"""Generated from Smithy shape ``com.amazonaws.workdocs#PermissionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.role_permission_type
    import capo_workdocs.types.role_type


class PermissionInfo(TypedDict, closed=True):
    role: NotRequired["capo_workdocs.types.role_type.RoleType"]
    """<p>The role of the user.</p>"""
    type: NotRequired["capo_workdocs.types.role_permission_type.RolePermissionType"]
    """<p>The type of permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionInfo) -> dict:
    out: dict = {}
    if "role" in value:
        import capo_workdocs.types.role_type

        out["Role"] = capo_workdocs.types.role_type.serialize_json(value["role"])
    if "type" in value:
        import capo_workdocs.types.role_permission_type

        out["Type"] = capo_workdocs.types.role_permission_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> PermissionInfo:
    out: PermissionInfo = {}  # type: ignore[typeddict-item]
    if "Role" in data:
        import capo_workdocs.types.role_type

        out["role"] = capo_workdocs.types.role_type.deserialize_json(data["Role"])
    if "Type" in data:
        import capo_workdocs.types.role_permission_type

        out["type"] = capo_workdocs.types.role_permission_type.deserialize_json(
            data["Type"]
        )
    return out
