"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutTargetsResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.error_code
    import capo_cloudwatch_events.types.error_message
    import capo_cloudwatch_events.types.target_id


class PutTargetsResultEntry(TypedDict, closed=True):
    target_id: NotRequired["capo_cloudwatch_events.types.target_id.TargetId"]
    """<p>The ID of the target.</p>"""
    error_code: NotRequired["capo_cloudwatch_events.types.error_code.ErrorCode"]
    """<p>The error code that indicates why the target addition failed. If the value is <code>ConcurrentModificationException</code>, too many requests were made at the same time.</p>"""
    error_message: NotRequired[
        "capo_cloudwatch_events.types.error_message.ErrorMessage"
    ]
    """<p>The error message that explains why the target addition failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutTargetsResultEntry) -> dict:
    out: dict = {}
    if "target_id" in value:
        out["TargetId"] = value["target_id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutTargetsResultEntry:
    out: PutTargetsResultEntry = {}  # type: ignore[typeddict-item]
    if "TargetId" in data:
        out["target_id"] = data["TargetId"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
