"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetNumericComparisonFilterCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_numeric_comparison_filter_operator
    import aws_sdk_quicksight.types.data_set_numeric_filter_value


class DataSetNumericComparisonFilterCondition(TypedDict, closed=True):
    operator: "aws_sdk_quicksight.types.data_set_numeric_comparison_filter_operator.DataSetNumericComparisonFilterOperator"
    """<p>The comparison operator to use, such as <code>EQUALS</code>, <code>GREATER_THAN</code>, <code>LESS_THAN</code>, or their variants.</p>"""
    value: NotRequired[
        "aws_sdk_quicksight.types.data_set_numeric_filter_value.DataSetNumericFilterValue"
    ]
    """<p>The numeric value to compare against.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetNumericComparisonFilterCondition) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.data_set_numeric_comparison_filter_operator

    out["Operator"] = (
        aws_sdk_quicksight.types.data_set_numeric_comparison_filter_operator.serialize_json(
            value["operator"]
        )
    )
    if "value" in value:
        import aws_sdk_quicksight.types.data_set_numeric_filter_value

        out["Value"] = (
            aws_sdk_quicksight.types.data_set_numeric_filter_value.serialize_json(
                value["value"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetNumericComparisonFilterCondition:
    out: DataSetNumericComparisonFilterCondition = {}  # type: ignore[typeddict-item]
    if "Operator" in data:
        import aws_sdk_quicksight.types.data_set_numeric_comparison_filter_operator

        out["operator"] = (
            aws_sdk_quicksight.types.data_set_numeric_comparison_filter_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError(
            "DataSetNumericComparisonFilterCondition.operator required"
        )
    if "Value" in data:
        import aws_sdk_quicksight.types.data_set_numeric_filter_value

        out["value"] = (
            aws_sdk_quicksight.types.data_set_numeric_filter_value.deserialize_json(
                data["Value"]
            )
        )
    return out
