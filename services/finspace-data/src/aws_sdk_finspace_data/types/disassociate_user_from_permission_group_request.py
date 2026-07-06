"""Generated from Smithy shape ``com.amazonaws.finspacedata#DisassociateUserFromPermissionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.client_token
    import aws_sdk_finspace_data.types.permission_group_id
    import aws_sdk_finspace_data.types.user_id


class DisassociateUserFromPermissionGroupRequest(TypedDict, closed=True):
    permission_group_id: (
        "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId"
    )
    """<p>The unique identifier for the permission group.</p>"""
    user_id: "aws_sdk_finspace_data.types.user_id.UserId"
    """<p>The unique identifier for the user.</p>"""
    client_token: NotRequired["aws_sdk_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateUserFromPermissionGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateUserFromPermissionGroupRequest:
    out: DisassociateUserFromPermissionGroupRequest = {}  # type: ignore[typeddict-item]
    return out
