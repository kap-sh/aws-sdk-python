"""Generated from Smithy shape ``com.amazonaws.sso#ListAccountRolesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso.types.next_token_type
    import aws_sdk_sso.types.role_list_type


class ListAccountRolesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sso.types.next_token_type.NextTokenType"]
    """<p>The page token client that is used to retrieve the list of accounts.</p>"""
    role_list: NotRequired["aws_sdk_sso.types.role_list_type.RoleListType"]
    """<p>A paginated response with the list of roles and the next token if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountRolesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "role_list" in value:
        import aws_sdk_sso.types.role_list_type

        out["roleList"] = aws_sdk_sso.types.role_list_type.serialize_json(
            value["role_list"]
        )
    return out


def deserialize_json(data: dict) -> ListAccountRolesResponse:
    out: ListAccountRolesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "roleList" in data:
        import aws_sdk_sso.types.role_list_type

        out["role_list"] = aws_sdk_sso.types.role_list_type.deserialize_json(
            data["roleList"]
        )
    return out
