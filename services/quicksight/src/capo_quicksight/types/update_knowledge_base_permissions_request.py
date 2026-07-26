"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateKnowledgeBasePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.kb_aws_account_id
    import capo_quicksight.types.knowledge_base_id
    import capo_quicksight.types.resource_permission_list


class UpdateKnowledgeBasePermissionsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.kb_aws_account_id.KbAwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the knowledge base.</p>"""
    knowledge_base_id: "capo_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier for the knowledge base.</p>"""
    grant_permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The resource permissions that you want to grant on the knowledge base.</p>"""
    revoke_permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The resource permissions that you want to revoke from the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKnowledgeBasePermissionsRequest) -> dict:
    out: dict = {}
    if "grant_permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["GrantPermissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["grant_permissions"]
            )
        )
    if "revoke_permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["RevokePermissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["revoke_permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKnowledgeBasePermissionsRequest:
    out: UpdateKnowledgeBasePermissionsRequest = {}  # type: ignore[typeddict-item]
    if "GrantPermissions" in data:
        import capo_quicksight.types.resource_permission_list

        out["grant_permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["GrantPermissions"]
            )
        )
    if "RevokePermissions" in data:
        import capo_quicksight.types.resource_permission_list

        out["revoke_permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["RevokePermissions"]
            )
        )
    return out
