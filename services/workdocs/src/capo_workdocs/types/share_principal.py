"""Generated from Smithy shape ``com.amazonaws.workdocs#SharePrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workdocs.types.id_type
    import capo_workdocs.types.principal_type
    import capo_workdocs.types.role_type


class SharePrincipal(TypedDict, closed=True):
    id: "capo_workdocs.types.id_type.IdType"
    """<p>The ID of the recipient.</p>"""
    type: "capo_workdocs.types.principal_type.PrincipalType"
    """<p>The type of the recipient.</p>"""
    role: "capo_workdocs.types.role_type.RoleType"
    """<p>The role of the recipient.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharePrincipal) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_workdocs.types.principal_type

    out["Type"] = capo_workdocs.types.principal_type.serialize_json(value["type"])
    import capo_workdocs.types.role_type

    out["Role"] = capo_workdocs.types.role_type.serialize_json(value["role"])
    return out


def deserialize_json(data: dict) -> SharePrincipal:
    out: SharePrincipal = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("SharePrincipal.id required")
    if "Type" in data:
        import capo_workdocs.types.principal_type

        out["type"] = capo_workdocs.types.principal_type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("SharePrincipal.type required")
    if "Role" in data:
        import capo_workdocs.types.role_type

        out["role"] = capo_workdocs.types.role_type.deserialize_json(data["Role"])
    else:
        raise DeserializationError("SharePrincipal.role required")
    return out
