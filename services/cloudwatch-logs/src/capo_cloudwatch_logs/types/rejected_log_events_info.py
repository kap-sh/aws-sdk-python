"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#RejectedLogEventsInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_event_index


class RejectedLogEventsInfo(TypedDict, closed=True):
    too_new_log_event_start_index: NotRequired[
        "capo_cloudwatch_logs.types.log_event_index.LogEventIndex"
    ]
    """<p>The index of the first log event that is too new. This field is inclusive.</p>"""
    too_old_log_event_end_index: NotRequired[
        "capo_cloudwatch_logs.types.log_event_index.LogEventIndex"
    ]
    """<p>The index of the last log event that is too old. This field is exclusive.</p>"""
    expired_log_event_end_index: NotRequired[
        "capo_cloudwatch_logs.types.log_event_index.LogEventIndex"
    ]
    """<p>The expired log events.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RejectedLogEventsInfo) -> dict:
    out: dict = {}
    if "too_new_log_event_start_index" in value:
        out["tooNewLogEventStartIndex"] = value["too_new_log_event_start_index"]
    if "too_old_log_event_end_index" in value:
        out["tooOldLogEventEndIndex"] = value["too_old_log_event_end_index"]
    if "expired_log_event_end_index" in value:
        out["expiredLogEventEndIndex"] = value["expired_log_event_end_index"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RejectedLogEventsInfo:
    out: RejectedLogEventsInfo = {}  # type: ignore[typeddict-item]
    if "tooNewLogEventStartIndex" in data:
        out["too_new_log_event_start_index"] = data["tooNewLogEventStartIndex"]
    if "tooOldLogEventEndIndex" in data:
        out["too_old_log_event_end_index"] = data["tooOldLogEventEndIndex"]
    if "expiredLogEventEndIndex" in data:
        out["expired_log_event_end_index"] = data["expiredLogEventEndIndex"]
    return out
