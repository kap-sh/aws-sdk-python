"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LiveTailSessionUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.live_tail_session_metadata
    import aws_sdk_cloudwatch_logs.types.live_tail_session_results


class LiveTailSessionUpdate(TypedDict):
    session_metadata: NotRequired[
        "aws_sdk_cloudwatch_logs.types.live_tail_session_metadata.LiveTailSessionMetadata"
    ]
    """<p>This object contains the session metadata for a Live Tail session.</p>"""
    session_results: NotRequired[
        "aws_sdk_cloudwatch_logs.types.live_tail_session_results.LiveTailSessionResults"
    ]
    """<p>An array, where each member of the array includes the information for one log event in the Live Tail session.</p> <p>A <code>sessionResults</code> array can include as many as 500 log events. If the number of log events matching the request exceeds 500 per second, the log events are sampled down to 500 log events to be included in each <code>sessionUpdate</code> structure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LiveTailSessionUpdate) -> dict:
    out: dict = {}
    if "session_metadata" in value:
        import aws_sdk_cloudwatch_logs.types.live_tail_session_metadata

        out["sessionMetadata"] = (
            aws_sdk_cloudwatch_logs.types.live_tail_session_metadata.serialize_aws_json_1_1(
                value["session_metadata"]
            )
        )
    if "session_results" in value:
        import aws_sdk_cloudwatch_logs.types.live_tail_session_results

        out["sessionResults"] = (
            aws_sdk_cloudwatch_logs.types.live_tail_session_results.serialize_aws_json_1_1(
                value["session_results"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LiveTailSessionUpdate:
    out: LiveTailSessionUpdate = {}  # type: ignore[typeddict-item]
    if "sessionMetadata" in data:
        import aws_sdk_cloudwatch_logs.types.live_tail_session_metadata

        out["session_metadata"] = (
            aws_sdk_cloudwatch_logs.types.live_tail_session_metadata.deserialize_aws_json_1_1(
                data["sessionMetadata"]
            )
        )
    if "sessionResults" in data:
        import aws_sdk_cloudwatch_logs.types.live_tail_session_results

        out["session_results"] = (
            aws_sdk_cloudwatch_logs.types.live_tail_session_results.deserialize_aws_json_1_1(
                data["sessionResults"]
            )
        )
    return out
