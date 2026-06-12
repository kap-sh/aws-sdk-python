"""Generated from Smithy shape ``com.amazonaws.workdocs#Principal``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.permission_info_list
    import aws_sdk_workdocs.types.principal_type


class Principal(TypedDict):
    id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The ID of the resource.</p>"""
    type: NotRequired["aws_sdk_workdocs.types.principal_type.PrincipalType"]
    """<p>The type of resource.</p>"""
    roles: NotRequired["aws_sdk_workdocs.types.permission_info_list.PermissionInfoList"]
    """<p>The permission information for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Principal) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import aws_sdk_workdocs.types.principal_type

        out["Type"] = aws_sdk_workdocs.types.principal_type.serialize_json(
            value["type"]
        )
    if "roles" in value:
        import aws_sdk_workdocs.types.permission_info_list

        out["Roles"] = aws_sdk_workdocs.types.permission_info_list.serialize_json(
            value["roles"]
        )
    return out


def deserialize_json(data: dict) -> Principal:
    out: Principal = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        import aws_sdk_workdocs.types.principal_type

        out["type"] = aws_sdk_workdocs.types.principal_type.deserialize_json(
            data["Type"]
        )
    if "Roles" in data:
        import aws_sdk_workdocs.types.permission_info_list

        out["roles"] = aws_sdk_workdocs.types.permission_info_list.deserialize_json(
            data["Roles"]
        )
    return out
