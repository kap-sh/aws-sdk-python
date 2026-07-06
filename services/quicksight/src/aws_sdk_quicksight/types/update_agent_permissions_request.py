"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAgentPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent_id
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.update_agent_permissions_request_grant_permissions_list
    import aws_sdk_quicksight.types.update_agent_permissions_request_revoke_permissions_list


class UpdateAgentPermissionsRequest(TypedDict, closed=True):
    agent_id: "aws_sdk_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the agent.</p>"""
    grant_permissions: NotRequired[
        "aws_sdk_quicksight.types.update_agent_permissions_request_grant_permissions_list.UpdateAgentPermissionsRequestGrantPermissionsList"
    ]
    """<p>The resource permissions that you want to grant on the agent.</p>"""
    revoke_permissions: NotRequired[
        "aws_sdk_quicksight.types.update_agent_permissions_request_revoke_permissions_list.UpdateAgentPermissionsRequestRevokePermissionsList"
    ]
    """<p>The resource permissions that you want to revoke from the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentPermissionsRequest) -> dict:
    out: dict = {}
    if "grant_permissions" in value:
        import aws_sdk_quicksight.types.update_agent_permissions_request_grant_permissions_list

        out["GrantPermissions"] = (
            aws_sdk_quicksight.types.update_agent_permissions_request_grant_permissions_list.serialize_json(
                value["grant_permissions"]
            )
        )
    if "revoke_permissions" in value:
        import aws_sdk_quicksight.types.update_agent_permissions_request_revoke_permissions_list

        out["RevokePermissions"] = (
            aws_sdk_quicksight.types.update_agent_permissions_request_revoke_permissions_list.serialize_json(
                value["revoke_permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentPermissionsRequest:
    out: UpdateAgentPermissionsRequest = {}  # type: ignore[typeddict-item]
    if "GrantPermissions" in data:
        import aws_sdk_quicksight.types.update_agent_permissions_request_grant_permissions_list

        out["grant_permissions"] = (
            aws_sdk_quicksight.types.update_agent_permissions_request_grant_permissions_list.deserialize_json(
                data["GrantPermissions"]
            )
        )
    if "RevokePermissions" in data:
        import aws_sdk_quicksight.types.update_agent_permissions_request_revoke_permissions_list

        out["revoke_permissions"] = (
            aws_sdk_quicksight.types.update_agent_permissions_request_revoke_permissions_list.deserialize_json(
                data["RevokePermissions"]
            )
        )
    return out
