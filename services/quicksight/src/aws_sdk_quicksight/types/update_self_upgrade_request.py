"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSelfUpgradeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.self_upgrade_admin_action
    import aws_sdk_quicksight.types.string


class UpdateSelfUpgradeRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the self-upgrade request.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The Quick namespace for the self-upgrade request.</p>"""
    upgrade_request_id: "aws_sdk_quicksight.types.string.String"
    """<p>The ID of the self-upgrade request to update.</p>"""
    action: "aws_sdk_quicksight.types.self_upgrade_admin_action.SelfUpgradeAdminAction"
    """<p>The action to perform on the self-upgrade request. Valid values are <code>APPROVE</code>, <code>DENY</code>, or <code>VERIFY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSelfUpgradeRequest) -> dict:
    out: dict = {}
    out["UpgradeRequestId"] = value["upgrade_request_id"]
    import aws_sdk_quicksight.types.self_upgrade_admin_action

    out["Action"] = aws_sdk_quicksight.types.self_upgrade_admin_action.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSelfUpgradeRequest:
    out: UpdateSelfUpgradeRequest = {}  # type: ignore[typeddict-item]
    if "UpgradeRequestId" in data:
        out["upgrade_request_id"] = data["UpgradeRequestId"]
    else:
        raise DeserializationError(
            "UpdateSelfUpgradeRequest.upgrade_request_id required"
        )
    if "Action" in data:
        import aws_sdk_quicksight.types.self_upgrade_admin_action

        out["action"] = (
            aws_sdk_quicksight.types.self_upgrade_admin_action.deserialize_json(
                data["Action"]
            )
        )
    else:
        raise DeserializationError("UpdateSelfUpgradeRequest.action required")
    return out
