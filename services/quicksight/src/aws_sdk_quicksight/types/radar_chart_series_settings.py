"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartSeriesSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.radar_chart_area_style_settings


class RadarChartSeriesSettings(TypedDict, closed=True):
    area_style_settings: NotRequired[
        "aws_sdk_quicksight.types.radar_chart_area_style_settings.RadarChartAreaStyleSettings"
    ]
    """<p>The area style settings of a radar chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RadarChartSeriesSettings) -> dict:
    out: dict = {}
    if "area_style_settings" in value:
        import aws_sdk_quicksight.types.radar_chart_area_style_settings

        out["AreaStyleSettings"] = (
            aws_sdk_quicksight.types.radar_chart_area_style_settings.serialize_json(
                value["area_style_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> RadarChartSeriesSettings:
    out: RadarChartSeriesSettings = {}  # type: ignore[typeddict-item]
    if "AreaStyleSettings" in data:
        import aws_sdk_quicksight.types.radar_chart_area_style_settings

        out["area_style_settings"] = (
            aws_sdk_quicksight.types.radar_chart_area_style_settings.deserialize_json(
                data["AreaStyleSettings"]
            )
        )
    return out
