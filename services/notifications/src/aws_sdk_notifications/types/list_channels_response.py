"""Generated from Smithy shape ``com.amazonaws.notifications#ListChannelsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_notifications.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_notifications.types.channels
    import aws_sdk_notifications.types.next_token

class ListChannelsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    channels: "aws_sdk_notifications.types.channels.Channels"
    """<p>A list of Channels.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_notifications.types.channels
    out["channels"] = aws_sdk_notifications.types.channels.serialize_json(value["channels"])
    return out


def deserialize_json(data: dict) -> ListChannelsResponse:
    out: ListChannelsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "channels" in data:
        import aws_sdk_notifications.types.channels
        out["channels"] = aws_sdk_notifications.types.channels.deserialize_json(data["channels"])
    else:
        raise DeserializationError("ListChannelsResponse.channels required")
    return out