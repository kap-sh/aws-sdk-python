"""Generated from Smithy shape ``com.amazonaws.quicksight#ComboChartSeriesSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.border_settings
    import aws_sdk_quicksight.types.decal_settings
    import aws_sdk_quicksight.types.line_chart_line_style_settings
    import aws_sdk_quicksight.types.line_chart_marker_style_settings


class ComboChartSeriesSettings(TypedDict):
    line_style_settings: NotRequired[
        "aws_sdk_quicksight.types.line_chart_line_style_settings.LineChartLineStyleSettings"
    ]
    """<p>Line styles options for the line series in the visual.</p>"""
    marker_style_settings: NotRequired[
        "aws_sdk_quicksight.types.line_chart_marker_style_settings.LineChartMarkerStyleSettings"
    ]
    """<p>Marker styles options for the line series in the visual.</p>"""
    decal_settings: NotRequired["aws_sdk_quicksight.types.decal_settings.DecalSettings"]
    """<p>Decal settings for the series in the visual.</p>"""
    border_settings: NotRequired[
        "aws_sdk_quicksight.types.border_settings.BorderSettings"
    ]
    """<p>Border settings for the bar series in the visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComboChartSeriesSettings) -> dict:
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
    if "border_settings" in value:
        import aws_sdk_quicksight.types.border_settings

        out["BorderSettings"] = aws_sdk_quicksight.types.border_settings.serialize_json(
            value["border_settings"]
        )
    return out


def deserialize_json(data: dict) -> ComboChartSeriesSettings:
    out: ComboChartSeriesSettings = {}  # type: ignore[typeddict-item]
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
    if "BorderSettings" in data:
        import aws_sdk_quicksight.types.border_settings

        out["border_settings"] = (
            aws_sdk_quicksight.types.border_settings.deserialize_json(
                data["BorderSettings"]
            )
        )
    return out
