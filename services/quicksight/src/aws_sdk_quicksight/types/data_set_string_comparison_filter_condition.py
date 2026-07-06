"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringComparisonFilterCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_string_comparison_filter_operator
    import aws_sdk_quicksight.types.data_set_string_filter_value


class DataSetStringComparisonFilterCondition(TypedDict, closed=True):
    operator: "aws_sdk_quicksight.types.data_set_string_comparison_filter_operator.DataSetStringComparisonFilterOperator"
    """<p>The comparison operator to use, such as <code>EQUALS</code>, <code>CONTAINS</code>, <code>STARTS_WITH</code>, <code>ENDS_WITH</code>, or their negations.</p>"""
    value: NotRequired[
        "aws_sdk_quicksight.types.data_set_string_filter_value.DataSetStringFilterValue"
    ]
    """<p>The string value to compare against.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetStringComparisonFilterCondition) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.data_set_string_comparison_filter_operator

    out["Operator"] = (
        aws_sdk_quicksight.types.data_set_string_comparison_filter_operator.serialize_json(
            value["operator"]
        )
    )
    if "value" in value:
        import aws_sdk_quicksight.types.data_set_string_filter_value

        out["Value"] = (
            aws_sdk_quicksight.types.data_set_string_filter_value.serialize_json(
                value["value"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetStringComparisonFilterCondition:
    out: DataSetStringComparisonFilterCondition = {}  # type: ignore[typeddict-item]
    if "Operator" in data:
        import aws_sdk_quicksight.types.data_set_string_comparison_filter_operator

        out["operator"] = (
            aws_sdk_quicksight.types.data_set_string_comparison_filter_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError(
            "DataSetStringComparisonFilterCondition.operator required"
        )
    if "Value" in data:
        import aws_sdk_quicksight.types.data_set_string_filter_value

        out["value"] = (
            aws_sdk_quicksight.types.data_set_string_filter_value.deserialize_json(
                data["Value"]
            )
        )
    return out
