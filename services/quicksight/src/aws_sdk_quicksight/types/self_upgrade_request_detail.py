"""Generated from Smithy shape ``com.amazonaws.quicksight#SelfUpgradeRequestDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.long
    import aws_sdk_quicksight.types.self_upgrade_request_status
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.user_name
    import aws_sdk_quicksight.types.user_role


class SelfUpgradeRequestDetail(TypedDict, closed=True):
    upgrade_request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The ID of the self-upgrade request.</p>"""
    user_name: NotRequired["aws_sdk_quicksight.types.user_name.UserName"]
    """<p>The username of the user who initiated the self-upgrade request.</p>"""
    original_role: NotRequired["aws_sdk_quicksight.types.user_role.UserRole"]
    """<p>The original role of the user before the upgrade.</p>"""
    requested_role: NotRequired["aws_sdk_quicksight.types.user_role.UserRole"]
    """<p>The role that the user is requesting to upgrade to.</p>"""
    request_note: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>An optional note explaining the reason for the self-upgrade request.</p>"""
    creation_time: "aws_sdk_quicksight.types.long.Long"
    """<p>The time when the self-upgrade request was created.</p>"""
    request_status: NotRequired[
        "aws_sdk_quicksight.types.self_upgrade_request_status.SelfUpgradeRequestStatus"
    ]
    """<p>The status of the self-upgrade request.</p>"""
    last_update_attempt_time: "aws_sdk_quicksight.types.long.Long"
    """<p>The time of the last update attempt for the self-upgrade request.</p>"""
    last_update_failure_reason: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The reason for the last update failure, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfUpgradeRequestDetail) -> dict:
    out: dict = {}
    if "upgrade_request_id" in value:
        out["UpgradeRequestId"] = value["upgrade_request_id"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "original_role" in value:
        import aws_sdk_quicksight.types.user_role

        out["OriginalRole"] = aws_sdk_quicksight.types.user_role.serialize_json(
            value["original_role"]
        )
    if "requested_role" in value:
        import aws_sdk_quicksight.types.user_role

        out["RequestedRole"] = aws_sdk_quicksight.types.user_role.serialize_json(
            value["requested_role"]
        )
    if "request_note" in value:
        out["RequestNote"] = value["request_note"]
    out["CreationTime"] = value.get("creation_time", 0)
    if "request_status" in value:
        import aws_sdk_quicksight.types.self_upgrade_request_status

        out["RequestStatus"] = (
            aws_sdk_quicksight.types.self_upgrade_request_status.serialize_json(
                value["request_status"]
            )
        )
    out["lastUpdateAttemptTime"] = value.get("last_update_attempt_time", 0)
    if "last_update_failure_reason" in value:
        out["lastUpdateFailureReason"] = value["last_update_failure_reason"]
    return out


def deserialize_json(data: dict) -> SelfUpgradeRequestDetail:
    out: SelfUpgradeRequestDetail = {}  # type: ignore[typeddict-item]
    if "UpgradeRequestId" in data:
        out["upgrade_request_id"] = data["UpgradeRequestId"]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "OriginalRole" in data:
        import aws_sdk_quicksight.types.user_role

        out["original_role"] = aws_sdk_quicksight.types.user_role.deserialize_json(
            data["OriginalRole"]
        )
    if "RequestedRole" in data:
        import aws_sdk_quicksight.types.user_role

        out["requested_role"] = aws_sdk_quicksight.types.user_role.deserialize_json(
            data["RequestedRole"]
        )
    if "RequestNote" in data:
        out["request_note"] = data["RequestNote"]
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    else:
        out["creation_time"] = 0
    if "RequestStatus" in data:
        import aws_sdk_quicksight.types.self_upgrade_request_status

        out["request_status"] = (
            aws_sdk_quicksight.types.self_upgrade_request_status.deserialize_json(
                data["RequestStatus"]
            )
        )
    if "lastUpdateAttemptTime" in data:
        out["last_update_attempt_time"] = data["lastUpdateAttemptTime"]
    else:
        out["last_update_attempt_time"] = 0
    if "lastUpdateFailureReason" in data:
        out["last_update_failure_reason"] = data["lastUpdateFailureReason"]
    return out
