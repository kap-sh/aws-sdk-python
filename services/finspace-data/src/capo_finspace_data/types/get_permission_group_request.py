"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetPermissionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.permission_group_id


class GetPermissionGroupRequest(TypedDict, closed=True):
    permission_group_id: (
        "capo_finspace_data.types.permission_group_id.PermissionGroupId"
    )
    """<p>The unique identifier for the permission group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPermissionGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPermissionGroupRequest:
    out: GetPermissionGroupRequest = {}  # type: ignore[typeddict-item]
    return out
