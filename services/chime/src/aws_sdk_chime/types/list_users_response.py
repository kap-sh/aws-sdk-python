"""Generated from Smithy shape ``com.amazonaws.chime#ListUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.string
    import aws_sdk_chime.types.user_list


class ListUsersResponse(TypedDict, closed=True):
    users: NotRequired["aws_sdk_chime.types.user_list.UserList"]
    """<p>List of users and user details.</p>"""
    next_token: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import aws_sdk_chime.types.user_list

        out["Users"] = aws_sdk_chime.types.user_list.serialize_json(value["users"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if "Users" in data:
        import aws_sdk_chime.types.user_list

        out["users"] = aws_sdk_chime.types.user_list.deserialize_json(data["Users"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
