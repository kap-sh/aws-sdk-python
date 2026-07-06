"""Generated from Smithy shape ``com.amazonaws.workdocs#SharePrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.principal_type
    import aws_sdk_workdocs.types.role_type


class SharePrincipal(TypedDict, closed=True):
    id: "aws_sdk_workdocs.types.id_type.IdType"
    """<p>The ID of the recipient.</p>"""
    type: "aws_sdk_workdocs.types.principal_type.PrincipalType"
    """<p>The type of the recipient.</p>"""
    role: "aws_sdk_workdocs.types.role_type.RoleType"
    """<p>The role of the recipient.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharePrincipal) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import aws_sdk_workdocs.types.principal_type

    out["Type"] = aws_sdk_workdocs.types.principal_type.serialize_json(value["type"])
    import aws_sdk_workdocs.types.role_type

    out["Role"] = aws_sdk_workdocs.types.role_type.serialize_json(value["role"])
    return out


def deserialize_json(data: dict) -> SharePrincipal:
    out: SharePrincipal = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("SharePrincipal.id required")
    if "Type" in data:
        import aws_sdk_workdocs.types.principal_type

        out["type"] = aws_sdk_workdocs.types.principal_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("SharePrincipal.type required")
    if "Role" in data:
        import aws_sdk_workdocs.types.role_type

        out["role"] = aws_sdk_workdocs.types.role_type.deserialize_json(data["Role"])
    else:
        raise DeserializationError("SharePrincipal.role required")
    return out
