"""Generated from Smithy shape ``com.amazonaws.wickr#ListBlockedGuestUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.blocked_guest_user_list
    import aws_sdk_wickr.types.generic_string


class ListBlockedGuestUsersResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""
    blocklist: "aws_sdk_wickr.types.blocked_guest_user_list.BlockedGuestUserList"
    """<p>A list of blocked guest user objects within the current page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBlockedGuestUsersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_wickr.types.blocked_guest_user_list

    out["blocklist"] = aws_sdk_wickr.types.blocked_guest_user_list.serialize_json(
        value["blocklist"]
    )
    return out


def deserialize_json(data: dict) -> ListBlockedGuestUsersResponse:
    out: ListBlockedGuestUsersResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "blocklist" in data:
        import aws_sdk_wickr.types.blocked_guest_user_list

        out["blocklist"] = aws_sdk_wickr.types.blocked_guest_user_list.deserialize_json(
            data["blocklist"]
        )
    else:
        raise DeserializationError("ListBlockedGuestUsersResponse.blocklist required")
    return out
