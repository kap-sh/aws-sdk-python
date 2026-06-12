"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListUsersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.pagination_token
    import aws_sdk_finspace_data.types.user_list


class ListUsersResponse(TypedDict):
    users: NotRequired["aws_sdk_finspace_data.types.user_list.UserList"]
    """<p>A list of all the users.</p>"""
    next_token: NotRequired[
        "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
    ]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import aws_sdk_finspace_data.types.user_list

        out["users"] = aws_sdk_finspace_data.types.user_list.serialize_json(
            value["users"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if "users" in data:
        import aws_sdk_finspace_data.types.user_list

        out["users"] = aws_sdk_finspace_data.types.user_list.deserialize_json(
            data["users"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
