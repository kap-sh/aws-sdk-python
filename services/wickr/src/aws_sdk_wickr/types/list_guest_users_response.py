"""Generated from Smithy shape ``com.amazonaws.wickr#ListGuestUsersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.guest_user_list


class ListGuestUsersResponse(TypedDict):
    next_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""
    guestlist: "aws_sdk_wickr.types.guest_user_list.GuestUserList"
    """<p>A list of guest user objects within the current page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGuestUsersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_wickr.types.guest_user_list

    out["guestlist"] = aws_sdk_wickr.types.guest_user_list.serialize_json(
        value["guestlist"]
    )
    return out


def deserialize_json(data: dict) -> ListGuestUsersResponse:
    out: ListGuestUsersResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "guestlist" in data:
        import aws_sdk_wickr.types.guest_user_list

        out["guestlist"] = aws_sdk_wickr.types.guest_user_list.deserialize_json(
            data["guestlist"]
        )
    else:
        raise DeserializationError("ListGuestUsersResponse.guestlist required")
    return out
