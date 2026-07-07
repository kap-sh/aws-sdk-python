"""Generated from Smithy shape ``com.amazonaws.wickr#ListSecurityGroupUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.users


class ListSecurityGroupUsersResponse(TypedDict, closed=True):
    users: "aws_sdk_wickr.types.users.Users"
    """<p>A list of user objects belonging to the security group within the current page.</p>"""
    next_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityGroupUsersResponse) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.users

    out["users"] = aws_sdk_wickr.types.users.serialize_json(value["users"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSecurityGroupUsersResponse:
    out: ListSecurityGroupUsersResponse = {}  # type: ignore[typeddict-item]
    if "users" in data:
        import aws_sdk_wickr.types.users

        out["users"] = aws_sdk_wickr.types.users.deserialize_json(data["users"])
    else:
        raise DeserializationError("ListSecurityGroupUsersResponse.users required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
