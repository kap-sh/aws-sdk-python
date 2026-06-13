"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringListFilterCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_string_list_filter_operator
    import aws_sdk_quicksight.types.data_set_string_list_filter_value


class DataSetStringListFilterCondition(TypedDict):
    operator: "aws_sdk_quicksight.types.data_set_string_list_filter_operator.DataSetStringListFilterOperator"
    """<p>The list operator to use, either <code>INCLUDE</code> to match values in the list or <code>EXCLUDE</code> to filter out values in the list.</p>"""
    values: NotRequired[
        "aws_sdk_quicksight.types.data_set_string_list_filter_value.DataSetStringListFilterValue"
    ]
    """<p>The list of string values to include or exclude in the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetStringListFilterCondition) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.data_set_string_list_filter_operator

    out["Operator"] = (
        aws_sdk_quicksight.types.data_set_string_list_filter_operator.serialize_json(
            value["operator"]
        )
    )
    if "values" in value:
        import aws_sdk_quicksight.types.data_set_string_list_filter_value

        out["Values"] = (
            aws_sdk_quicksight.types.data_set_string_list_filter_value.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetStringListFilterCondition:
    out: DataSetStringListFilterCondition = {}  # type: ignore[typeddict-item]
    if "Operator" in data:
        import aws_sdk_quicksight.types.data_set_string_list_filter_operator

        out["operator"] = (
            aws_sdk_quicksight.types.data_set_string_list_filter_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("DataSetStringListFilterCondition.operator required")
    if "Values" in data:
        import aws_sdk_quicksight.types.data_set_string_list_filter_value

        out["values"] = (
            aws_sdk_quicksight.types.data_set_string_list_filter_value.deserialize_json(
                data["Values"]
            )
        )
    return out
