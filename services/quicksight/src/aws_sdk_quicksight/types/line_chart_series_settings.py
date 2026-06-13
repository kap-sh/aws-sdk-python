"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartSeriesSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.decal_settings
    import aws_sdk_quicksight.types.line_chart_line_style_settings
    import aws_sdk_quicksight.types.line_chart_marker_style_settings


class LineChartSeriesSettings(TypedDict):
    line_style_settings: NotRequired[
        "aws_sdk_quicksight.types.line_chart_line_style_settings.LineChartLineStyleSettings"
    ]
    """<p>Line styles options for a line series in <code>LineChartVisual</code>.</p>"""
    marker_style_settings: NotRequired[
        "aws_sdk_quicksight.types.line_chart_marker_style_settings.LineChartMarkerStyleSettings"
    ]
    """<p>Marker styles options for a line series in <code>LineChartVisual</code>.</p>"""
    decal_settings: NotRequired["aws_sdk_quicksight.types.decal_settings.DecalSettings"]
    """<p>Decal settings for a line series in <code>LineChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineChartSeriesSettings) -> dict:
    out: dict = {}
    if "line_style_settings" in value:
        import aws_sdk_quicksight.types.line_chart_line_style_settings

        out["LineStyleSettings"] = (
            aws_sdk_quicksight.types.line_chart_line_style_settings.serialize_json(
                value["line_style_settings"]
            )
        )
    if "marker_style_settings" in value:
        import aws_sdk_quicksight.types.line_chart_marker_style_settings

        out["MarkerStyleSettings"] = (
            aws_sdk_quicksight.types.line_chart_marker_style_settings.serialize_json(
                value["marker_style_settings"]
            )
        )
    if "decal_settings" in value:
        import aws_sdk_quicksight.types.decal_settings

        out["DecalSettings"] = aws_sdk_quicksight.types.decal_settings.serialize_json(
            value["decal_settings"]
        )
    return out


def deserialize_json(data: dict) -> LineChartSeriesSettings:
    out: LineChartSeriesSettings = {}  # type: ignore[typeddict-item]
    if "LineStyleSettings" in data:
        import aws_sdk_quicksight.types.line_chart_line_style_settings

        out["line_style_settings"] = (
            aws_sdk_quicksight.types.line_chart_line_style_settings.deserialize_json(
                data["LineStyleSettings"]
            )
        )
    if "MarkerStyleSettings" in data:
        import aws_sdk_quicksight.types.line_chart_marker_style_settings

        out["marker_style_settings"] = (
            aws_sdk_quicksight.types.line_chart_marker_style_settings.deserialize_json(
                data["MarkerStyleSettings"]
            )
        )
    if "DecalSettings" in data:
        import aws_sdk_quicksight.types.decal_settings

        out["decal_settings"] = (
            aws_sdk_quicksight.types.decal_settings.deserialize_json(
                data["DecalSettings"]
            )
        )
    return out
