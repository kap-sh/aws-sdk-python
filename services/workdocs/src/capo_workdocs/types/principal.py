"""Generated from Smithy shape ``com.amazonaws.workdocs#Principal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.id_type
    import capo_workdocs.types.permission_info_list
    import capo_workdocs.types.principal_type


class Principal(TypedDict, closed=True):
    id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the resource.</p>"""
    type: NotRequired["capo_workdocs.types.principal_type.PrincipalType"]
    """<p>The type of resource.</p>"""
    roles: NotRequired["capo_workdocs.types.permission_info_list.PermissionInfoList"]
    """<p>The permission information for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Principal) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_workdocs.types.principal_type

        out["Type"] = capo_workdocs.types.principal_type.serialize_json(value["type"])
    if "roles" in value:
        import capo_workdocs.types.permission_info_list

        out["Roles"] = capo_workdocs.types.permission_info_list.serialize_json(
            value["roles"]
        )
    return out


def deserialize_json(data: dict) -> Principal:
    out: Principal = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        import capo_workdocs.types.principal_type

        out["type"] = capo_workdocs.types.principal_type.deserialize_json(data["Type"])
    if "Roles" in data:
        import capo_workdocs.types.permission_info_list

        out["roles"] = capo_workdocs.types.permission_info_list.deserialize_json(
            data["Roles"]
        )
    return out
