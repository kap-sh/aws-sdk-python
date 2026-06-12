"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchPrincipalType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.search_principal_role_list


class SearchPrincipalType(TypedDict):
    id: "aws_sdk_workdocs.types.id_type.IdType"
    """<p>UserIds or GroupIds.</p>"""
    roles: NotRequired[
        "aws_sdk_workdocs.types.search_principal_role_list.SearchPrincipalRoleList"
    ]
    """<p>The Role of a User or Group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPrincipalType) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "roles" in value:
        import aws_sdk_workdocs.types.search_principal_role_list

        out["Roles"] = aws_sdk_workdocs.types.search_principal_role_list.serialize_json(
            value["roles"]
        )
    return out


def deserialize_json(data: dict) -> SearchPrincipalType:
    out: SearchPrincipalType = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("SearchPrincipalType.id required")
    if "Roles" in data:
        import aws_sdk_workdocs.types.search_principal_role_list

        out["roles"] = (
            aws_sdk_workdocs.types.search_principal_role_list.deserialize_json(
                data["Roles"]
            )
        )
    return out
