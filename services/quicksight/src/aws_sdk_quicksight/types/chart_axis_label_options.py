"""Generated from Smithy shape ``com.amazonaws.quicksight#ChartAxisLabelOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.axis_label_options_list
    import aws_sdk_quicksight.types.visibility


class ChartAxisLabelOptions(TypedDict):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility of an axis label on a chart. Choose one of the following options:</p> <ul> <li> <p> <code>VISIBLE</code>: Shows the axis.</p> </li> <li> <p> <code>HIDDEN</code>: Hides the axis.</p> </li> </ul>"""
    sort_icon_visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility configuration of the sort icon on a chart's axis label.</p>"""
    axis_label_options: NotRequired[
        "aws_sdk_quicksight.types.axis_label_options_list.AxisLabelOptionsList"
    ]
    """<p>The label options for a chart axis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChartAxisLabelOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "sort_icon_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["SortIconVisibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["sort_icon_visibility"]
        )
    if "axis_label_options" in value:
        import aws_sdk_quicksight.types.axis_label_options_list

        out["AxisLabelOptions"] = (
            aws_sdk_quicksight.types.axis_label_options_list.serialize_json(
                value["axis_label_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChartAxisLabelOptions:
    out: ChartAxisLabelOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "SortIconVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["sort_icon_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["SortIconVisibility"]
            )
        )
    if "AxisLabelOptions" in data:
        import aws_sdk_quicksight.types.axis_label_options_list

        out["axis_label_options"] = (
            aws_sdk_quicksight.types.axis_label_options_list.deserialize_json(
                data["AxisLabelOptions"]
            )
        )
    return out
