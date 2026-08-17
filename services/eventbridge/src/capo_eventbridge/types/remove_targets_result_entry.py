"""Generated from Smithy shape ``com.amazonaws.eventbridge#RemoveTargetsResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.error_code
    import capo_eventbridge.types.error_message
    import capo_eventbridge.types.target_id


class RemoveTargetsResultEntry(TypedDict, closed=True):
    target_id: NotRequired["capo_eventbridge.types.target_id.TargetId"]
    """<p>The ID of the target.</p>"""
    error_code: NotRequired["capo_eventbridge.types.error_code.ErrorCode"]
    """<p>The error code that indicates why the target removal failed. If the value is <code>ConcurrentModificationException</code>, too many requests were made at the same time.</p>"""
    error_message: NotRequired["capo_eventbridge.types.error_message.ErrorMessage"]
    """<p>The error message that explains why the target removal failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTargetsResultEntry) -> dict:
    out: dict = {}
    if "target_id" in value:
        out["TargetId"] = value["target_id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTargetsResultEntry:
    out: RemoveTargetsResultEntry = {}  # type: ignore[typeddict-item]
    if data.get("TargetId") is not None:
        out["target_id"] = data["TargetId"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
