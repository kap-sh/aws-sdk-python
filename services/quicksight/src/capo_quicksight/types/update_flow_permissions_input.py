"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateFlowPermissionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.account_id
    import capo_quicksight.types.flow_id
    import capo_quicksight.types.update_flow_permissions_input_grant_permissions_list
    import capo_quicksight.types.update_flow_permissions_input_revoke_permissions_list


class UpdateFlowPermissionsInput(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account that contains the flow you are updating permissions against.</p>"""
    flow_id: "capo_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow to update permissions for.</p>"""
    grant_permissions: NotRequired[
        "capo_quicksight.types.update_flow_permissions_input_grant_permissions_list.UpdateFlowPermissionsInputGrantPermissionsList"
    ]
    """<p>The permissions that you want to grant on this flow.</p>"""
    revoke_permissions: NotRequired[
        "capo_quicksight.types.update_flow_permissions_input_revoke_permissions_list.UpdateFlowPermissionsInputRevokePermissionsList"
    ]
    """<p>The permissions that you want to revoke from this flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowPermissionsInput) -> dict:
    out: dict = {}
    if "grant_permissions" in value:
        import capo_quicksight.types.update_flow_permissions_input_grant_permissions_list

        out["GrantPermissions"] = (
            capo_quicksight.types.update_flow_permissions_input_grant_permissions_list.serialize_json(
                value["grant_permissions"]
            )
        )
    if "revoke_permissions" in value:
        import capo_quicksight.types.update_flow_permissions_input_revoke_permissions_list

        out["RevokePermissions"] = (
            capo_quicksight.types.update_flow_permissions_input_revoke_permissions_list.serialize_json(
                value["revoke_permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateFlowPermissionsInput:
    out: UpdateFlowPermissionsInput = {}  # type: ignore[typeddict-item]
    if "GrantPermissions" in data:
        import capo_quicksight.types.update_flow_permissions_input_grant_permissions_list

        out["grant_permissions"] = (
            capo_quicksight.types.update_flow_permissions_input_grant_permissions_list.deserialize_json(
                data["GrantPermissions"]
            )
        )
    if "RevokePermissions" in data:
        import capo_quicksight.types.update_flow_permissions_input_revoke_permissions_list

        out["revoke_permissions"] = (
            capo_quicksight.types.update_flow_permissions_input_revoke_permissions_list.deserialize_json(
                data["RevokePermissions"]
            )
        )
    return out
