"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RemoveTargetsResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.error_code
    import aws_sdk_cloudwatch_events.types.error_message
    import aws_sdk_cloudwatch_events.types.target_id


class RemoveTargetsResultEntry(TypedDict, closed=True):
    target_id: NotRequired["aws_sdk_cloudwatch_events.types.target_id.TargetId"]
    """<p>The ID of the target.</p>"""
    error_code: NotRequired["aws_sdk_cloudwatch_events.types.error_code.ErrorCode"]
    """<p>The error code that indicates why the target removal failed. If the value is <code>ConcurrentModificationException</code>, too many requests were made at the same time.</p>"""
    error_message: NotRequired[
        "aws_sdk_cloudwatch_events.types.error_message.ErrorMessage"
    ]
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
    if "TargetId" in data:
        out["target_id"] = data["TargetId"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
