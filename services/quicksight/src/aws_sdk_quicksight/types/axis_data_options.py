"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisDataOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.date_axis_options
    import aws_sdk_quicksight.types.numeric_axis_options


class AxisDataOptions(TypedDict, closed=True):
    numeric_axis_options: NotRequired[
        "aws_sdk_quicksight.types.numeric_axis_options.NumericAxisOptions"
    ]
    """<p>The options for an axis with a numeric field.</p>"""
    date_axis_options: NotRequired[
        "aws_sdk_quicksight.types.date_axis_options.DateAxisOptions"
    ]
    """<p>The options for an axis with a date field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisDataOptions) -> dict:
    out: dict = {}
    if "numeric_axis_options" in value:
        import aws_sdk_quicksight.types.numeric_axis_options

        out["NumericAxisOptions"] = (
            aws_sdk_quicksight.types.numeric_axis_options.serialize_json(
                value["numeric_axis_options"]
            )
        )
    if "date_axis_options" in value:
        import aws_sdk_quicksight.types.date_axis_options

        out["DateAxisOptions"] = (
            aws_sdk_quicksight.types.date_axis_options.serialize_json(
                value["date_axis_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> AxisDataOptions:
    out: AxisDataOptions = {}  # type: ignore[typeddict-item]
    if "NumericAxisOptions" in data:
        import aws_sdk_quicksight.types.numeric_axis_options

        out["numeric_axis_options"] = (
            aws_sdk_quicksight.types.numeric_axis_options.deserialize_json(
                data["NumericAxisOptions"]
            )
        )
    if "DateAxisOptions" in data:
        import aws_sdk_quicksight.types.date_axis_options

        out["date_axis_options"] = (
            aws_sdk_quicksight.types.date_axis_options.deserialize_json(
                data["DateAxisOptions"]
            )
        )
    return out
