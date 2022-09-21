"""Contains the Bokeh Model for the HighStock pane"""
from collections import OrderedDict
from typing import List, Optional

from .highbase import PATH_HIGH_CHARTS, PATH_REQUIRE_HIGH_CHARTS, PATHS, HighBase


class HighStock(HighBase):
    """The Bokeh Model for the HighStock pane"""

    __javascript__ = [
        "https://cdn.highcharts.com.cn/highcharts.js",
        "https://cdn.highcharts.com.cn/modules/stock.js",
        "https://cdn.highcharts.com.cn/modules/export-data.js",
        "https://cdn.highcharts.com.cn/highcharts/modules/exporting.js",
        "https://code.highcharts.com.cn/highcharts-plugins/highcharts-zh_CN.js",
    ]

    # https://api.highcharts.com/class-reference/#toc5
    __js_require__ = {
        "packages": [
            {
                "name": "highcharts",
                "main": "highcharts",
            },
        ],
        "paths": {
            "highcharts": "https://cdn.highcharts.com.cn",
            "highcharts/modules/stock": "https://cdn.highcharts.com.cn/modules/stock",
            "highcharts/modules/exporting": "https://cdn.highcharts.com.cn/modules/exporting",
            "highcharts/modules/export-data": "https://cdn.highcharts.com.cn/modules/export-data",
        },
        "exports": {
            "highcharts": "Highcharts",
            "highcharts/modules/stock": "highchartsmodulesstock",
            "highcharts/modules/exporting": "highchartsmodulesexporting",
            "highcharts/modules/export-data": "highchartsmodulesexportdata",
        },
    }

    @classmethod
    def js_files(  # pylint: disable=too-many-locals, too-many-arguments
        cls,
        highcharts_accessibility: bool = False,
        highcharts_annotations: bool = False,
        highcharts_boost: bool = False,
        highcharts_broken_axis: bool = False,
        highcharts_canvas_tools: bool = False,
        highcharts_data: bool = False,
        highcharts_drilldown: bool = False,
        highcharts_export_data: bool = True,
        highcharts_exporting: bool = True,
        highcharts_more: bool = False,
        highcharts_no_data: bool = False,
        highcharts_offline_exporting: bool = False,
        highcharts_solid_gauge: bool = False,
        others: Optional[List] = None
    ):
        """Configures the js files to include from https://code.highcharts.com.cn

        Use this before using `panel.extension("highchart")`

        Args:
            highcharts_accessibility (bool, optional): Defaults to False.
            highcharts_annotations (bool, optional): Defaults to False.
            highcharts_boost (bool, optional): Defaults to False.
            highcharts_broken_axis (bool, optional): Defaults to False.
            highcharts_canvas_tools (bool, optional): Defaults to False.
            highcharts_data (bool, optional): Defaults to False.
            highcharts_drilldown (bool, optional): Defaults to False.
            highcharts_export_data (bool, optional): Defaults to True.
            highcharts_exporting (bool, optional): Defaults to True.
            highcharts_more (bool, optional): Defaults to False.
            highcharts_networkgraph (bool, optional): Defaults to False.
            highcharts_no_data (bool, optional): Defaults to False.
            highcharts_offline_exporting (bool, optional): Defaults to False.
            highcharts_solid_gauge (bool, optional): Defaults to False.
            others (list, optional): a list of key that are defined in highbase.PATHS to be set to True.
        """
        paths = OrderedDict()
        others = others or []
        include = {
            "highcharts/modules/stock": True,
            "highcharts-more": highcharts_more,
            "highcharts/modules/accessibility": highcharts_accessibility,
            "highcharts/modules/annotations": highcharts_annotations,
            "highcharts/modules/boost": highcharts_boost,
            "highcharts/modules/broken-axis": highcharts_broken_axis,
            "highcharts/modules/canvas-tools": highcharts_canvas_tools,
            "highcharts/modules/data": highcharts_data,
            "highcharts/modules/drilldown": highcharts_drilldown,
            "highcharts/modules/export-data": highcharts_export_data,
            "highcharts/modules/exporting": highcharts_exporting,
            "highcharts/modules/no-data": highcharts_no_data,
            "highcharts/modules/offline-exporting": highcharts_offline_exporting,
            "highcharts/modules/solid-gauge": highcharts_solid_gauge,
            **{k: True for k in others},
        }
        for key, value in include.items():
            if value:
                paths[key] = PATHS[key]

        cls.__javascript__ = cls.__javascript__ + list(paths.values())
        cls.__js_require__["paths"] = {
            "highcharts": PATH_REQUIRE_HIGH_CHARTS,
            **cls.__js_require__["paths"],
            **{k: v[:-3] for k, v in paths.items()},
        }
        cls.__js_require__["exports"] = {
            "highcharts": "Highcharts",
            **{k: k.replace("/", "").replace("-", "") for k in paths},  # type: ignore
        }
