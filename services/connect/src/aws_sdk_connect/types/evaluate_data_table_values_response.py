"""Generated from Smithy shape ``com.amazonaws.connect#EvaluateDataTableValuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_evaluated_value_list
    import aws_sdk_connect.types.next_token


class EvaluateDataTableValuesResponse(TypedDict, closed=True):
    values: "aws_sdk_connect.types.data_table_evaluated_value_list.DataTableEvaluatedValueList"
    """<p>A list of evaluated values with their computed results, error information, and metadata.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateDataTableValuesResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.data_table_evaluated_value_list

    out["Values"] = (
        aws_sdk_connect.types.data_table_evaluated_value_list.serialize_json(
            value["values"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> EvaluateDataTableValuesResponse:
    out: EvaluateDataTableValuesResponse = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import aws_sdk_connect.types.data_table_evaluated_value_list

        out["values"] = (
            aws_sdk_connect.types.data_table_evaluated_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("EvaluateDataTableValuesResponse.values required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
