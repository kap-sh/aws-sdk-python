"""Generated from Smithy shape ``com.amazonaws.finspacedata#DeletePermissionGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.client_token
    import aws_sdk_finspace_data.types.permission_group_id


class DeletePermissionGroupRequest(TypedDict):
    permission_group_id: (
        "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId"
    )
    """<p>The unique identifier for the permission group that you want to delete.</p>"""
    client_token: NotRequired["aws_sdk_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePermissionGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePermissionGroupRequest:
    out: DeletePermissionGroupRequest = {}  # type: ignore[typeddict-item]
    return out
