"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_user_list
    import aws_sdk_finspace.types.pagination_token


class ListKxUsersResponse(TypedDict, closed=True):
    users: NotRequired["aws_sdk_finspace.types.kx_user_list.KxUserList"]
    """<p>A list of users in a kdb environment.</p>"""
    next_token: NotRequired["aws_sdk_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import aws_sdk_finspace.types.kx_user_list

        out["users"] = aws_sdk_finspace.types.kx_user_list.serialize_json(
            value["users"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKxUsersResponse:
    out: ListKxUsersResponse = {}  # type: ignore[typeddict-item]
    if "users" in data:
        import aws_sdk_finspace.types.kx_user_list

        out["users"] = aws_sdk_finspace.types.kx_user_list.deserialize_json(
            data["users"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
