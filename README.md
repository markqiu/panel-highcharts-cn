![Panel HighCharts Logo](https://raw.githubusercontent.com/markqiu/panel-highcharts-cn/main/assets/images/panel-highcharts-logo.png)

[![PyPI version](https://badge.fury.io/py/panel-sketch.svg)](https://pypi.org/project/panel-highcharts/) [![Downloads](https://pepy.tech/badge/panel-highcharts/month)](https://pepy.tech/project/panel-highcharts) ![Python Versions](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue) ![PyPI - License](https://img.shields.io/pypi/l/panel-highcharts) ![Style Black](https://warehouse-camo.ingress.cmh1.psfhosted.org/fbfdc7754183ecf079bc71ddeabaf88f6cbc5c00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667)

[![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)

# panel-highcharts的中文版本
1. 采用highcharts.com.cn的中文版js，全面支持中文
2. 调通了highcharts.com.cn上的一些中文例子


# &#128200; Panel HighCharts

The `panel-highcharts` package makes it easy to use [Highcharts](https://www.highcharts.com/) from Python for exploratory analysis in a Jupyter Notebook or as a [HoloViz Panel](https://panel.holoviz.org) Web App.

Check out the `panel-highcharts` examples on **Binder** or the article [Highly Interactive Data Visualization](https://towardsdatascience.com/highly-interactive-data-visualization-cd3a9b082370).

| Jupyter Notebook | Jupyter Labs | Panel Apps |
| - | - | - |
| [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel) |

[<img src="https://raw.githubusercontent.com/markqiu/panel-highcharts-cn/main/assets/images/panel-highcharts-binder.gif" alt="Panel HighChart Reference Example" style="max-width:100%;">](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/HighChart.ipynb)



## 🏁 Background

This project was started because a colleague of mine loves to use HighCharts for his analytics trading apps. As there was no really easy way of using HighCharts in Python, Notebooks or Panel, it would be difficult for me, my team and our traders to collaborate. So I created this package in my spare time as an open source project to share with the world.

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

![Basic Example](https://raw.githubusercontent.com/markqiu/panel-highcharts-cn/main/assets/images/panel-highcharts-basic-example.png)

### 👩‍🏫 Reference Guides

| Guide | Notebook | Jupyter Notebook | Jupyter Labs | Panel App |
| - | - | - | - | - |
| HighChart | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/HighChart.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/HighChart.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/HighChart.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/HighChart) |
| HighStock | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/HighStock.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/HighStock.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/HighStock.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/HighStock) |
| HighMap | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/HighMap.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/HighMap.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/HighMap.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/HighMap) |
| HighGantt | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/HighGantt.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/HighGantt.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/HighGantt.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/HighGantt) |

### 🎨 Gallery

| Guide | Notebook | Jupyter Notebook | Jupyter Labs | App | App
| - | - | - | - |- | - |
| AddSeriesDynamically | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/AddSeriesDynamically.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/AddSeriesDynamically.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/AddSeriesDynamically.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/AddSeriesDynamically) | |
| LinkedCharts | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/LinkedCharts.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/LinkedCharts.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/LinkedCharts.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/LinkedCharts) | |
| Network | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/Network.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/Network.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/Network.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/Network) | [Awesome Panel](https://awesome-panel.org/highcharts-network) |
| PackedBubble | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/PackedBubble.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/PackedBubble.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/PackedBubble.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/PackedBubble) | |
| Themes | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/Themes.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/Themes.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/Themes.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/Themes) | |
| Variwide | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/Variwide.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/Variwide.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/Variwide.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/Variwide) | |
| Y轴标示线 | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/Y轴标示线.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/Y轴标示线.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/Y轴标示线.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/Y轴标示线) | |
| 包含事件标志的图表 | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/包含事件标志的图表.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/包含事件标志的图表.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/包含事件标志的图表.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/包含事件标志的图表) | |
| 基础折线图 | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/基础折线图.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/基础折线图.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/基础折线图.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/基础折线图) | |
| 包含成交量的蜡烛图 | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/包含成交量的蜡烛图.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/包含成交量的蜡烛图.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/包含成交量的蜡烛图.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/包含成交量的蜡烛图) | |
| 包含多条数据 | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/包含多条数据.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/包含多条数据.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/包含多条数据.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/包含多条数据) | |
| 面积范围图 | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/面积范围图.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/面积范围图.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/面积范围图.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/面积范围图) | |
| MACD | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/MACD.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/MACD.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/MACD.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/MACD) | |
| SMA_VbP | [View](https://github.com/markqiu/panel-highcharts-cn/blob/main/examples/SMA_VbP.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?filepath=examples/SMA_VbP.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=lab/tree/examples/SMA_VbP.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/markqiu/panel-highcharts-cn/HEAD?urlpath=panel/SMA_VbP) | |

## 💡 Inspiration

You can find more inspiration via

- [Awesome Panel](https://awesome-panel.org)
- [Highcharts-cn](https://www.highcharts.com.cn), [Demos](https://www.highcharts.com.cn/demo)
- [Highly Interactive Data Visualization](https://towardsdatascience.com/highly-interactive-data-visualization-cd3a9b082370)
- [Panel](https://panel.holoviz.org)

## 🛣️ Roadmap

When I get the time I would like to

- Support pandas `.plot` api via method as `.highplot` on dataframes
- Add more examples
- Add badges for 100% test coverage etc.
- Distribute as conda package

## 📰 Change Log

- 20220901: 
  1. js_files函数增加others传参，可直接传入需要加载的js文件的keys列表。 
  2. 增加几个例子。
- 20220830: 增加中文例子。修改readme，增加中文说明。
- 20220822: 初始项目，增加中文插件
