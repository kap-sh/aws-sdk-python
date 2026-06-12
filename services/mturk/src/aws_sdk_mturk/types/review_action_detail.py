"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewActionDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mturk.types.entity_id
    import aws_sdk_mturk.types.review_action_status
    import aws_sdk_mturk.types.string
    import aws_sdk_mturk.types.timestamp


class ReviewActionDetail(TypedDict):
    action_id: NotRequired["aws_sdk_mturk.types.entity_id.EntityId"]
    """<p>The unique identifier for the action.</p>"""
    action_name: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> The nature of the action itself. The Review Policy is responsible for examining the HIT and Assignments, emitting results, and deciding which other actions will be necessary. </p>"""
    target_id: NotRequired["aws_sdk_mturk.types.entity_id.EntityId"]
    """<p> The specific HITId or AssignmentID targeted by the action.</p>"""
    target_type: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> The type of object in TargetId.</p>"""
    status: NotRequired["aws_sdk_mturk.types.review_action_status.ReviewActionStatus"]
    """<p> The current disposition of the action: INTENDED, SUCCEEDED, FAILED, or CANCELLED. </p>"""
    complete_time: NotRequired["aws_sdk_mturk.types.timestamp.Timestamp"]
    """<p> The date when the action was completed.</p>"""
    result: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> A description of the outcome of the review.</p>"""
    error_code: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> Present only when the Results have a FAILED Status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewActionDetail) -> dict:
    out: dict = {}
    if "action_id" in value:
        out["ActionId"] = value["action_id"]
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    if "target_id" in value:
        out["TargetId"] = value["target_id"]
    if "target_type" in value:
        out["TargetType"] = value["target_type"]
    if "status" in value:
        import aws_sdk_mturk.types.review_action_status

        out["Status"] = aws_sdk_mturk.types.review_action_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "complete_time" in value:
        import aws_sdk_mturk.types.timestamp

        out["CompleteTime"] = aws_sdk_mturk.types.timestamp.serialize_aws_json_1_1(
            value["complete_time"]
        )
    if "result" in value:
        out["Result"] = value["result"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReviewActionDetail:
    out: ReviewActionDetail = {}  # type: ignore[typeddict-item]
    if "ActionId" in data:
        out["action_id"] = data["ActionId"]
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
    if "TargetId" in data:
        out["target_id"] = data["TargetId"]
    if "TargetType" in data:
        out["target_type"] = data["TargetType"]
    if "Status" in data:
        import aws_sdk_mturk.types.review_action_status

        out["status"] = (
            aws_sdk_mturk.types.review_action_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CompleteTime" in data:
        import aws_sdk_mturk.types.timestamp

        out["complete_time"] = aws_sdk_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["CompleteTime"]
        )
    if "Result" in data:
        out["result"] = data["Result"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    return out
