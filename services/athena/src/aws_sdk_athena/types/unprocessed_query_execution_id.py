"""Generated from Smithy shape ``com.amazonaws.athena#UnprocessedQueryExecutionId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.error_code
    import aws_sdk_athena.types.error_message
    import aws_sdk_athena.types.query_execution_id


class UnprocessedQueryExecutionId(TypedDict, closed=True):
    query_execution_id: NotRequired[
        "aws_sdk_athena.types.query_execution_id.QueryExecutionId"
    ]
    """<p>The unique identifier of the query execution.</p>"""
    error_code: NotRequired["aws_sdk_athena.types.error_code.ErrorCode"]
    """<p>The error code returned when the query execution failed to process, if applicable.</p>"""
    error_message: NotRequired["aws_sdk_athena.types.error_message.ErrorMessage"]
    """<p>The error message returned when the query execution failed to process, if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedQueryExecutionId) -> dict:
    out: dict = {}
    if "query_execution_id" in value:
        out["QueryExecutionId"] = value["query_execution_id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnprocessedQueryExecutionId:
    out: UnprocessedQueryExecutionId = {}  # type: ignore[typeddict-item]
    if "QueryExecutionId" in data:
        out["query_execution_id"] = data["QueryExecutionId"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
