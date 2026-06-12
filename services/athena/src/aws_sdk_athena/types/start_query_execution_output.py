"""Generated from Smithy shape ``com.amazonaws.athena#StartQueryExecutionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.query_execution_id


class StartQueryExecutionOutput(TypedDict):
    query_execution_id: NotRequired[
        "aws_sdk_athena.types.query_execution_id.QueryExecutionId"
    ]
    """<p>The unique ID of the query that ran as a result of this request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartQueryExecutionOutput) -> dict:
    out: dict = {}
    if "query_execution_id" in value:
        out["QueryExecutionId"] = value["query_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartQueryExecutionOutput:
    out: StartQueryExecutionOutput = {}  # type: ignore[typeddict-item]
    if "QueryExecutionId" in data:
        out["query_execution_id"] = data["QueryExecutionId"]
    return out
