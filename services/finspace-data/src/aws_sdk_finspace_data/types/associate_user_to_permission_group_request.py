"""Generated from Smithy shape ``com.amazonaws.finspacedata#AssociateUserToPermissionGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.client_token
    import aws_sdk_finspace_data.types.permission_group_id
    import aws_sdk_finspace_data.types.user_id


class AssociateUserToPermissionGroupRequest(TypedDict):
    permission_group_id: (
        "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId"
    )
    """<p>The unique identifier for the permission group.</p>"""
    user_id: "aws_sdk_finspace_data.types.user_id.UserId"
    """<p>The unique identifier for the user.</p>"""
    client_token: NotRequired["aws_sdk_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateUserToPermissionGroupRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AssociateUserToPermissionGroupRequest:
    out: AssociateUserToPermissionGroupRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
