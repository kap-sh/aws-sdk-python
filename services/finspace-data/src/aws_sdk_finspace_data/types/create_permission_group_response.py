"""Generated from Smithy shape ``com.amazonaws.finspacedata#CreatePermissionGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.permission_group_id


class CreatePermissionGroupResponse(TypedDict, closed=True):
    permission_group_id: NotRequired[
        "aws_sdk_finspace_data.types.permission_group_id.PermissionGroupId"
    ]
    """<p>The unique identifier for the permission group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePermissionGroupResponse) -> dict:
    out: dict = {}
    if "permission_group_id" in value:
        out["permissionGroupId"] = value["permission_group_id"]
    return out


def deserialize_json(data: dict) -> CreatePermissionGroupResponse:
    out: CreatePermissionGroupResponse = {}  # type: ignore[typeddict-item]
    if "permissionGroupId" in data:
        out["permission_group_id"] = data["permissionGroupId"]
    return out
