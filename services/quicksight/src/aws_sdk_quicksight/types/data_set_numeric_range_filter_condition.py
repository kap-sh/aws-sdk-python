"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetNumericRangeFilterCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.data_set_numeric_filter_value


class DataSetNumericRangeFilterCondition(TypedDict):
    range_minimum: NotRequired[
        "aws_sdk_quicksight.types.data_set_numeric_filter_value.DataSetNumericFilterValue"
    ]
    """<p>The minimum numeric value for the range filter.</p>"""
    range_maximum: NotRequired[
        "aws_sdk_quicksight.types.data_set_numeric_filter_value.DataSetNumericFilterValue"
    ]
    """<p>The maximum numeric value for the range filter.</p>"""
    include_minimum: NotRequired["aws_sdk_quicksight.types.boolean.Boolean"]
    """<p>Whether to include the minimum value in the filter range.</p>"""
    include_maximum: NotRequired["aws_sdk_quicksight.types.boolean.Boolean"]
    """<p>Whether to include the maximum value in the filter range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetNumericRangeFilterCondition) -> dict:
    out: dict = {}
    if "range_minimum" in value:
        import aws_sdk_quicksight.types.data_set_numeric_filter_value

        out["RangeMinimum"] = (
            aws_sdk_quicksight.types.data_set_numeric_filter_value.serialize_json(
                value["range_minimum"]
            )
        )
    if "range_maximum" in value:
        import aws_sdk_quicksight.types.data_set_numeric_filter_value

        out["RangeMaximum"] = (
            aws_sdk_quicksight.types.data_set_numeric_filter_value.serialize_json(
                value["range_maximum"]
            )
        )
    if "include_minimum" in value:
        out["IncludeMinimum"] = value["include_minimum"]
    if "include_maximum" in value:
        out["IncludeMaximum"] = value["include_maximum"]
    return out


def deserialize_json(data: dict) -> DataSetNumericRangeFilterCondition:
    out: DataSetNumericRangeFilterCondition = {}  # type: ignore[typeddict-item]
    if "RangeMinimum" in data:
        import aws_sdk_quicksight.types.data_set_numeric_filter_value

        out["range_minimum"] = (
            aws_sdk_quicksight.types.data_set_numeric_filter_value.deserialize_json(
                data["RangeMinimum"]
            )
        )
    if "RangeMaximum" in data:
        import aws_sdk_quicksight.types.data_set_numeric_filter_value

        out["range_maximum"] = (
            aws_sdk_quicksight.types.data_set_numeric_filter_value.deserialize_json(
                data["RangeMaximum"]
            )
        )
    if "IncludeMinimum" in data:
        out["include_minimum"] = data["IncludeMinimum"]
    if "IncludeMaximum" in data:
        out["include_maximum"] = data["IncludeMaximum"]
    return out
