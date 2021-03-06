![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9-blue) [![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MarcSkovMadsen/panel-vegafusion/HEAD?urlpath=lab) [![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)

# Panel VegaFusion

WORK IN PROGRESS. PROOF OF CONCEPT WORKING.

The [Panel VegaFusion pane](https://github.com/marcskovmadsen/panel-vegafusion) allows you to create interactive **big data apps** based on the
[Altair](https://altair-viz.github.io/index.html)
plotting library and the [Vega](https://vega.github.io/vega/) visualization specification.

[VegaFusion](https://github.com/vegafusion/vegafusion) provides serverside acceleration for the
Vega visualization grammar.

[Panel](https://panel.holoviz.org/) makes it easy to create powerful  data apps using the tools you know and ❤️. Member of the [HoloViz](https://holoviz.org/) ecosystem.

![Reference Example](https://raw.githubusercontent.com/MarcSkovMadsen/panel-vegafusion/main/assets/panel-vegafusion.gif)

## Install

```bash
pip install panel-vegafusion
```

If you have Jupyter Lab installed and plan on using it you should definately also install the
[Panel Jupyterlab Preview](https://blog.holoviz.org/panel_0.12.0.html#JupyterLab-previews) via

```bash
jupyter serverextension enable panel.io.jupyter_server_extension
```

## Example

```python
import altair as alt
import panel as pn
from panel_vegafusion import VegaFusion
from panel_vegafusion.utils import get_plot, ALTAIR_BLUE, get_theme

pn.extension(template="fast")

theme=get_theme()
alt.themes.enable(theme)

plot=get_plot() # Can be replaced by any Altair plot or Vega Specification

component = VegaFusion(plot, height=800).servable()

pn.state.template.param.update(
    site="Panel VegaFusion", title="Interactive BIG DATA apps with CROSSFILTERING for Altair and Vega",
    accent_base_color=ALTAIR_BLUE, header_background=ALTAIR_BLUE,
)
```

You can serve the application via `panel serve name_of_file.py` or
`panel serve name_of_notebook.ipynb`. Add the `--autoreload` for *hot reload* during development
and `--show` to automatically open the app in the browser.

## License - AGPLv3 - IMPORTANT

This Panel Vegafusion project is AGPLv3 Licensed because VegaFusion is AGPLv3 licensed and *requires the
author to provide this application's source code upon request*.

SO PLEASE INVESTIGATE THE LEGAL ASPECTS ON YOUR OWN. YOU WILL BE USING THIS PROJECT AT YOUR OWN RISK ANYWAYS! 👍

[![Legal Statement](https://raw.githubusercontent.com/MarcSkovMadsen/panel-vegafusion/main/assets/legal-statement.png)]((https://github.com/vegafusion/vegafusion/issues/62#issuecomment-1024403557))

## References

- [VegaFusion Github](https://github.com/vegafusion/vegafusion) | [VegaFusion documentation](https://vegafusion.io/)
- [Panel Docs](https://panel.holoviz.org/) | [Panel Discourse](https://discourse.holoviz.org/) | [Awesome Panel](https://awesome-panel.org/)
- [DataShader](https://datashader.org/) | [hvplot](https://hvplot.holoviz.org/) | [HoloViews](https://holoviews.org/)

## Issues Identified

- [vegafusion/vegafusion #64 - Support Vega-Embed Themes](https://github.com/vegafusion/vegafusion/issues/64)
- [Bokeh Discourse - Cannot bokeh build extension with wasm dependency](https://discourse.bokeh.org/t/how-do-i-build-bokeh-extension-with-wasm-depencency/8842)
- [bokeh/ipywidgets_bokeh #46 - Not working with VegaFusionWidget](https://github.com/bokeh/ipywidgets_bokeh/issues/46)
- [holoviz/param #597 - Add edit_readonly](https://github.com/holoviz/param/issues/597)
- [holoviz/panel #3149 - Object of type Chart is not JSON serializable](https://github.com/holoviz/panel/issues/3149)
- [vegafusion/vegafusion #62 - Please support Panel](https://github.com/vegafusion/vegafusion/issues/62)
- [vegafusion/vegafusion #63 - Please provide simple .js build](https://github.com/vegafusion/vegafusion/issues/63)
- [vegafusion/vegafusion #68 - Provide VegaFusionRunTime from the vegafusion package](https://github.com/vegafusion/vegafusion/issues/68)
- [vegafusion/vegafusion #66 - Please support events](https://github.com/vegafusion/vegafusion/issues/66)
- [vegafusion/vegafusion #67 - Uncaught (in promise) out of memory](https://github.com/vegafusion/vegafusion/issues/67)
- [vegafusion/vegafusion #69 - Document how VegaFusion solves real problems](https://github.com/vegafusion/vegafusion/issues/69)
- [vegafusion/vegafusion #70 - Move feather transformer to 'vegafusion' package](https://github.com/vegafusion/vegafusion/issues/70)
- [vegafusion/vegafusion #67 - Support multiple 'vegafusion' renderers](https://github.com/vegafusion/vegafusion/issues/71)

## Develop

### Install for development

```bash
git clone https://github.com/MarcSkovMadsen/panel-vegafusion.git
conda create -n panel_vegafusion -c conda-forge python=3.9 nodejs
conda activate panel_vegafusion
pip install -e .[all]
cd src-js
npm install
cd ..
```

### Build

Javascript package

```bash
invoke build.js
```

Python package

```bash
invoke build.package
```

### Test

```bash
invoke test.all
```

### Serve Dev App

For now you can serve an example with hot reload via

```bash
panel serve 'tests/apps/test_dev_app.py' --autoreload --show
```

![Panel VegaFusion Test App](https://raw.githubusercontent.com/MarcSkovMadsen/panel-vegafusion/main/assets/panel-vegafusion-dev-test.gif)

### Serve Example Apps

For now you can serve an example with hot reload via

```bash
panel serve 'examples/*.py' --autoreload --show
```

### Reference

You can also find inspiration in the original Jupyter VegaFusion reference example via

```bash
jupyter lab tests/reference_example.ipynb
```

### Release Python Package

Before releasing please make sures you have

- updated all version numbers
- build all packages
- run all tests with succes

```bash
python -m twine upload dist/*<VERSION>*
```

to deploy the package 📦.

If you want to upload to `testpypi` first you can do so by adding `--repository testpypi`.
