![Panel HighCharts Logo](https://raw.githubusercontent.com/MarcSkovMadsen/panel-highcharts/main/assets/images/panel-highcharts-logo.png)

[![PyPI version](https://badge.fury.io/py/panel-sketch.svg)](https://pypi.org/project/panel-highcharts/) [![Downloads](https://pepy.tech/badge/panel-highcharts/month)](https://pepy.tech/project/panel-highcharts) ![Python Versions](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue) ![PyPI - License](https://img.shields.io/pypi/l/panel-highcharts) ![Style Black](https://warehouse-camo.ingress.cmh1.psfhosted.org/fbfdc7754183ecf079bc71ddeabaf88f6cbc5c00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667)

[![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)

# &#128200; Panel HighCharts

The `panel-highcharts` package makes it easy to use [Highcharts](https://www.highcharts.com/) from Python for exploratory analysis in a Jupyter Notebook or as a HoloViz [Panel](https://panel.holoviz.org) Web App.

Check out the `panel-highcharts` examples on **Binder**

| Jupyter Notebook | Jupyter Labs | Panel Apps |
| - | - | - |
| [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel) |

[![Panel HighChart Reference Example](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/assets/images/panel-highcharts-binder.gif?raw=true)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighChart.ipynb)

## 🏁 Background

This project was started because a colleague of mine loves to use HighCharts for his analytics trading apps. As there was no really easy way of using HighCharts in Python, Notebooks or Panel, it would be difficult for me, my team and our traders to collaborate. So I created this package as a private, open source project to share with the world.

## ⚖️ License

The `panel-highcharts` python package and repository is open source and free to use (MIT License), however **Highcharts itself requires a license for commercial use**. For more info see the Highcharts license [FAQs](https://shop.highsoft.com/faq).

## 🏃 Getting Started

With `pip`

```bash
pip install panel-highcharts
```

From within a Jupyter Notebook

```python
import panel_highcharts as ph

import panel as pn
pn.extension('highchart')
```

```python
configuration = {
    "title": {"text": "HighChart Pane"},
    "series": [
        {
            "name": "series1",
            "data": [1, 2, 3, 4, 5],
        }
    ]
}
```

```python
ph.HighChart(object=configuration, sizing_mode="stretch_width")
```

![Basic Example](assets/images/panel-highcharts-basic-example.png)

### 👩‍🏫 Reference Guides

| Guide | Notebook | Jupyter Notebook | Jupyter Labs | Panel App |
| - | - | - | - |-
| HighChart | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/HighChart.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/HighChart.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighChart.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/HighChart) |
| HighStock | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/HighStock.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/HighStock.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighStock.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/HighStock) |
| HighMap | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/HighMap.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/HighMap.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighMap.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/HighMap) |
| HighGantt | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/HighGantt.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/HighGantt.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/HighGantt.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/HighGantt) |

### 🎨 Gallery

| Guide | Notebook | Jupyter Notebook | Jupyter Labs | Panel App |
| - | - | - | - |-
| Network | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/Network.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/Network.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/Network.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/Network) |
| PackedBubble | [View](https://github.com/MarcSkovMadsen/panel-highcharts/blob/main/examples/PackedBubble.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?filepath=examples/PackedBubble.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=lab/tree/examples/PackedBubble.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcskovmadsen/panel-highcharts/HEAD?urlpath=panel/PackedBubble) |

## 💡 Inspiration

You can find more inspiration via

- [Awesome Panel](https://awesome-panel.org)
- [Highcharts](https://www.highcharts.com), [Demos](https://www.highcharts.com/demo)
- [Highly Interactive Data Visualization](https://towardsdatascience.com/highly-interactive-data-visualization-cd3a9b082370)
- [Panel](https://panel.holoviz.org)

## 🛣️ Roadmap

When I get the time I would like to

- Support pandas `.plot` api via method as `.highplot` on dataframes
- Add more examples
- Add badges for 100% test coverage etc.
- Distribute as conda package

## 📰 Change Log

- 20210405: Add HighStock, HighMap, HighGantt
- 20210404: Can now display in Classic Notebook
- 20210403: First Release to PyPi. Works in Jupyter Lab and Panel App.
