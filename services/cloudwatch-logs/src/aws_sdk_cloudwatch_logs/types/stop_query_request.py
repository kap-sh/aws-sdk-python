"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StopQueryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.query_id


class StopQueryRequest(TypedDict):
    query_id: "aws_sdk_cloudwatch_logs.types.query_id.QueryId"
    """<p>The ID number of the query to stop. To find this ID number, use <code>DescribeQueries</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopQueryRequest) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopQueryRequest:
    out: StopQueryRequest = {}  # type: ignore[typeddict-item]
    if "queryId" in data:
        out["query_id"] = data["queryId"]
    else:
        raise DeserializationError("StopQueryRequest.query_id required")
    return out
