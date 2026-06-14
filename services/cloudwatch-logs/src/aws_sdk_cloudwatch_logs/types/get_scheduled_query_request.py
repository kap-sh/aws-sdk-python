"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetScheduledQueryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.scheduled_query_identifier


class GetScheduledQueryRequest(TypedDict):
    identifier: "aws_sdk_cloudwatch_logs.types.scheduled_query_identifier.ScheduledQueryIdentifier"
    """<p>The ARN or name of the scheduled query to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetScheduledQueryRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetScheduledQueryRequest:
    out: GetScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("GetScheduledQueryRequest.identifier required")
    return out
