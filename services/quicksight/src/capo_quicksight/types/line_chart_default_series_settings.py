"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartDefaultSeriesSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_binding
    import capo_quicksight.types.decal_settings
    import capo_quicksight.types.line_chart_line_style_settings
    import capo_quicksight.types.line_chart_marker_style_settings


class LineChartDefaultSeriesSettings(TypedDict, closed=True):
    axis_binding: NotRequired["capo_quicksight.types.axis_binding.AxisBinding"]
    """<p>The axis to which you are binding all line series to.</p>"""
    line_style_settings: NotRequired[
        "capo_quicksight.types.line_chart_line_style_settings.LineChartLineStyleSettings"
    ]
    """<p>Line styles options for all line series in the visual.</p>"""
    marker_style_settings: NotRequired[
        "capo_quicksight.types.line_chart_marker_style_settings.LineChartMarkerStyleSettings"
    ]
    """<p>Marker styles options for all line series in the visual.</p>"""
    decal_settings: NotRequired["capo_quicksight.types.decal_settings.DecalSettings"]
    """<p>Decal settings options for all line series in the visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineChartDefaultSeriesSettings) -> dict:
    out: dict = {}
    if "axis_binding" in value:
        import capo_quicksight.types.axis_binding

        out["AxisBinding"] = capo_quicksight.types.axis_binding.serialize_json(
            value["axis_binding"]
        )
    if "line_style_settings" in value:
        import capo_quicksight.types.line_chart_line_style_settings

        out["LineStyleSettings"] = (
            capo_quicksight.types.line_chart_line_style_settings.serialize_json(
                value["line_style_settings"]
            )
        )
    if "marker_style_settings" in value:
        import capo_quicksight.types.line_chart_marker_style_settings

        out["MarkerStyleSettings"] = (
            capo_quicksight.types.line_chart_marker_style_settings.serialize_json(
                value["marker_style_settings"]
            )
        )
    if "decal_settings" in value:
        import capo_quicksight.types.decal_settings

        out["DecalSettings"] = capo_quicksight.types.decal_settings.serialize_json(
            value["decal_settings"]
        )
    return out


def deserialize_json(data: dict) -> LineChartDefaultSeriesSettings:
    out: LineChartDefaultSeriesSettings = {}  # type: ignore[typeddict-item]
    if "AxisBinding" in data:
        import capo_quicksight.types.axis_binding

        out["axis_binding"] = capo_quicksight.types.axis_binding.deserialize_json(
            data["AxisBinding"]
        )
    if "LineStyleSettings" in data:
        import capo_quicksight.types.line_chart_line_style_settings

        out["line_style_settings"] = (
            capo_quicksight.types.line_chart_line_style_settings.deserialize_json(
                data["LineStyleSettings"]
            )
        )
    if "MarkerStyleSettings" in data:
        import capo_quicksight.types.line_chart_marker_style_settings

        out["marker_style_settings"] = (
            capo_quicksight.types.line_chart_marker_style_settings.deserialize_json(
                data["MarkerStyleSettings"]
            )
        )
    if "DecalSettings" in data:
        import capo_quicksight.types.decal_settings

        out["decal_settings"] = capo_quicksight.types.decal_settings.deserialize_json(
            data["DecalSettings"]
        )
    return out
