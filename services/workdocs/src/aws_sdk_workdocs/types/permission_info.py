"""Generated from Smithy shape ``com.amazonaws.workdocs#PermissionInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.role_permission_type
    import aws_sdk_workdocs.types.role_type


class PermissionInfo(TypedDict):
    role: NotRequired["aws_sdk_workdocs.types.role_type.RoleType"]
    """<p>The role of the user.</p>"""
    type: NotRequired["aws_sdk_workdocs.types.role_permission_type.RolePermissionType"]
    """<p>The type of permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionInfo) -> dict:
    out: dict = {}
    if "role" in value:
        import aws_sdk_workdocs.types.role_type

        out["Role"] = aws_sdk_workdocs.types.role_type.serialize_json(value["role"])
    if "type" in value:
        import aws_sdk_workdocs.types.role_permission_type

        out["Type"] = aws_sdk_workdocs.types.role_permission_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> PermissionInfo:
    out: PermissionInfo = {}  # type: ignore[typeddict-item]
    if "Role" in data:
        import aws_sdk_workdocs.types.role_type

        out["role"] = aws_sdk_workdocs.types.role_type.deserialize_json(data["Role"])
    if "Type" in data:
        import aws_sdk_workdocs.types.role_permission_type

        out["type"] = aws_sdk_workdocs.types.role_permission_type.deserialize_json(
            data["Type"]
        )
    return out
