"""Generated from Smithy shape ``com.amazonaws.wickr#ListUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.users


class ListUsersResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""
    users: NotRequired["aws_sdk_wickr.types.users.Users"]
    """<p>A list of user objects matching the specified filters and within the current page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "users" in value:
        import aws_sdk_wickr.types.users

        out["users"] = aws_sdk_wickr.types.users.serialize_json(value["users"])
    return out


def deserialize_json(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "users" in data:
        import aws_sdk_wickr.types.users

        out["users"] = aws_sdk_wickr.types.users.deserialize_json(data["users"])
    return out
