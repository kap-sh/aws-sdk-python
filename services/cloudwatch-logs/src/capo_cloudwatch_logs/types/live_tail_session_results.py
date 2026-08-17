"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LiveTailSessionResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.live_tail_session_log_event

LiveTailSessionResults: TypeAlias = list[
    "capo_cloudwatch_logs.types.live_tail_session_log_event.LiveTailSessionLogEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LiveTailSessionResults) -> list:
    import capo_cloudwatch_logs.types.live_tail_session_log_event

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.live_tail_session_log_event.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LiveTailSessionResults:
    import capo_cloudwatch_logs.types.live_tail_session_log_event

    out: LiveTailSessionResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.live_tail_session_log_event.deserialize_aws_json_1_1(
                item
            )
        )
    return out
