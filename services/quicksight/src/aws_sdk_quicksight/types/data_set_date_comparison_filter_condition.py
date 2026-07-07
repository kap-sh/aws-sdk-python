"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetDateComparisonFilterCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_date_comparison_filter_operator
    import aws_sdk_quicksight.types.data_set_date_filter_value


class DataSetDateComparisonFilterCondition(TypedDict, closed=True):
    operator: "aws_sdk_quicksight.types.data_set_date_comparison_filter_operator.DataSetDateComparisonFilterOperator"
    """<p>The comparison operator to use, such as <code>BEFORE</code>, <code>BEFORE_OR_EQUALS_TO</code>, <code>AFTER</code>, or <code>AFTER_OR_EQUALS_TO</code>.</p>"""
    value: NotRequired[
        "aws_sdk_quicksight.types.data_set_date_filter_value.DataSetDateFilterValue"
    ]
    """<p>The date value to compare against.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetDateComparisonFilterCondition) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.data_set_date_comparison_filter_operator

    out["Operator"] = (
        aws_sdk_quicksight.types.data_set_date_comparison_filter_operator.serialize_json(
            value["operator"]
        )
    )
    if "value" in value:
        import aws_sdk_quicksight.types.data_set_date_filter_value

        out["Value"] = (
            aws_sdk_quicksight.types.data_set_date_filter_value.serialize_json(
                value["value"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetDateComparisonFilterCondition:
    out: DataSetDateComparisonFilterCondition = {}  # type: ignore[typeddict-item]
    if "Operator" in data:
        import aws_sdk_quicksight.types.data_set_date_comparison_filter_operator

        out["operator"] = (
            aws_sdk_quicksight.types.data_set_date_comparison_filter_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError(
            "DataSetDateComparisonFilterCondition.operator required"
        )
    if "Value" in data:
        import aws_sdk_quicksight.types.data_set_date_filter_value

        out["value"] = (
            aws_sdk_quicksight.types.data_set_date_filter_value.deserialize_json(
                data["Value"]
            )
        )
    return out
