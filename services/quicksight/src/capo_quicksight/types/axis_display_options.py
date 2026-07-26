"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisDisplayOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_data_options
    import capo_quicksight.types.axis_tick_label_options
    import capo_quicksight.types.pixel_length
    import capo_quicksight.types.scroll_bar_options
    import capo_quicksight.types.visibility


class AxisDisplayOptions(TypedDict, closed=True):
    tick_label_options: NotRequired[
        "capo_quicksight.types.axis_tick_label_options.AxisTickLabelOptions"
    ]
    """<p>The tick label options of an axis.</p>"""
    axis_line_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Determines whether or not the axis line is visible.</p>"""
    grid_line_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Determines whether or not the grid line is visible.</p>"""
    data_options: NotRequired["capo_quicksight.types.axis_data_options.AxisDataOptions"]
    """<p>The data options for an axis.</p>"""
    scrollbar_options: NotRequired[
        "capo_quicksight.types.scroll_bar_options.ScrollBarOptions"
    ]
    """<p>The scroll bar options for an axis.</p>"""
    axis_offset: NotRequired["capo_quicksight.types.pixel_length.PixelLength"]
    """<p>The offset value that determines the starting placement of the axis within a visual's bounds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisDisplayOptions) -> dict:
    out: dict = {}
    if "tick_label_options" in value:
        import capo_quicksight.types.axis_tick_label_options

        out["TickLabelOptions"] = (
            capo_quicksight.types.axis_tick_label_options.serialize_json(
                value["tick_label_options"]
            )
        )
    if "axis_line_visibility" in value:
        import capo_quicksight.types.visibility

        out["AxisLineVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["axis_line_visibility"]
        )
    if "grid_line_visibility" in value:
        import capo_quicksight.types.visibility

        out["GridLineVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["grid_line_visibility"]
        )
    if "data_options" in value:
        import capo_quicksight.types.axis_data_options

        out["DataOptions"] = capo_quicksight.types.axis_data_options.serialize_json(
            value["data_options"]
        )
    if "scrollbar_options" in value:
        import capo_quicksight.types.scroll_bar_options

        out["ScrollbarOptions"] = (
            capo_quicksight.types.scroll_bar_options.serialize_json(
                value["scrollbar_options"]
            )
        )
    if "axis_offset" in value:
        out["AxisOffset"] = value["axis_offset"]
    return out


def deserialize_json(data: dict) -> AxisDisplayOptions:
    out: AxisDisplayOptions = {}  # type: ignore[typeddict-item]
    if "TickLabelOptions" in data:
        import capo_quicksight.types.axis_tick_label_options

        out["tick_label_options"] = (
            capo_quicksight.types.axis_tick_label_options.deserialize_json(
                data["TickLabelOptions"]
            )
        )
    if "AxisLineVisibility" in data:
        import capo_quicksight.types.visibility

        out["axis_line_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["AxisLineVisibility"]
        )
    if "GridLineVisibility" in data:
        import capo_quicksight.types.visibility

        out["grid_line_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["GridLineVisibility"]
        )
    if "DataOptions" in data:
        import capo_quicksight.types.axis_data_options

        out["data_options"] = capo_quicksight.types.axis_data_options.deserialize_json(
            data["DataOptions"]
        )
    if "ScrollbarOptions" in data:
        import capo_quicksight.types.scroll_bar_options

        out["scrollbar_options"] = (
            capo_quicksight.types.scroll_bar_options.deserialize_json(
                data["ScrollbarOptions"]
            )
        )
    if "AxisOffset" in data:
        out["axis_offset"] = data["AxisOffset"]
    return out
