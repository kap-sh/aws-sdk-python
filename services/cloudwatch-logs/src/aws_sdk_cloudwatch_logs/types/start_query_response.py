"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StartQueryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.query_id


class StartQueryResponse(TypedDict):
    query_id: NotRequired["aws_sdk_cloudwatch_logs.types.query_id.QueryId"]
    """<p>The unique ID of the query. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartQueryResponse) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["queryId"] = value["query_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartQueryResponse:
    out: StartQueryResponse = {}  # type: ignore[typeddict-item]
    if "queryId" in data:
        out["query_id"] = data["queryId"]
    return out
