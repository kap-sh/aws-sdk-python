"""Generated from Smithy shape ``com.amazonaws.athena#GetQueryExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.query_execution_id


class GetQueryExecutionInput(TypedDict):
    query_execution_id: "aws_sdk_athena.types.query_execution_id.QueryExecutionId"
    """<p>The unique ID of the query execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQueryExecutionInput) -> dict:
    out: dict = {}
    out["QueryExecutionId"] = value["query_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQueryExecutionInput:
    out: GetQueryExecutionInput = {}  # type: ignore[typeddict-item]
    if "QueryExecutionId" in data:
        out["query_execution_id"] = data["QueryExecutionId"]
    else:
        raise DeserializationError("GetQueryExecutionInput.query_execution_id required")
    return out
