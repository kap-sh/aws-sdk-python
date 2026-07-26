"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetPermissionGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.permission_group


class GetPermissionGroupResponse(TypedDict, closed=True):
    permission_group: NotRequired[
        "capo_finspace_data.types.permission_group.PermissionGroup"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetPermissionGroupResponse) -> dict:
    out: dict = {}
    if "permission_group" in value:
        import capo_finspace_data.types.permission_group

        out["permissionGroup"] = (
            capo_finspace_data.types.permission_group.serialize_json(
                value["permission_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPermissionGroupResponse:
    out: GetPermissionGroupResponse = {}  # type: ignore[typeddict-item]
    if "permissionGroup" in data:
        import capo_finspace_data.types.permission_group

        out["permission_group"] = (
            capo_finspace_data.types.permission_group.deserialize_json(
                data["permissionGroup"]
            )
        )
    return out
