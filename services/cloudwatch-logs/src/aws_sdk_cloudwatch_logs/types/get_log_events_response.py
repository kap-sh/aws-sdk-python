"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.next_token
    import aws_sdk_cloudwatch_logs.types.output_log_events


class GetLogEventsResponse(TypedDict):
    events: NotRequired[
        "aws_sdk_cloudwatch_logs.types.output_log_events.OutputLogEvents"
    ]
    """<p>The events.</p>"""
    next_forward_token: NotRequired[
        "aws_sdk_cloudwatch_logs.types.next_token.NextToken"
    ]
    """<p>The token for the next set of items in the forward direction. The token expires after 24 hours. If you have reached the end of the stream, it returns the same token you passed in.</p>"""
    next_backward_token: NotRequired[
        "aws_sdk_cloudwatch_logs.types.next_token.NextToken"
    ]
    """<p>The token for the next set of items in the backward direction. The token expires after 24 hours. This token is not null. If you have reached the end of the stream, it returns the same token you passed in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogEventsResponse) -> dict:
    out: dict = {}
    if "events" in value:
        import aws_sdk_cloudwatch_logs.types.output_log_events

        out["events"] = (
            aws_sdk_cloudwatch_logs.types.output_log_events.serialize_aws_json_1_1(
                value["events"]
            )
        )
    if "next_forward_token" in value:
        out["nextForwardToken"] = value["next_forward_token"]
    if "next_backward_token" in value:
        out["nextBackwardToken"] = value["next_backward_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogEventsResponse:
    out: GetLogEventsResponse = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import aws_sdk_cloudwatch_logs.types.output_log_events

        out["events"] = (
            aws_sdk_cloudwatch_logs.types.output_log_events.deserialize_aws_json_1_1(
                data["events"]
            )
        )
    if "nextForwardToken" in data:
        out["next_forward_token"] = data["nextForwardToken"]
    if "nextBackwardToken" in data:
        out["next_backward_token"] = data["nextBackwardToken"]
    return out
