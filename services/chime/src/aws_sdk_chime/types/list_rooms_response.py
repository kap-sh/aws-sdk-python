"""Generated from Smithy shape ``com.amazonaws.chime#ListRoomsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.room_list
    import aws_sdk_chime.types.string


class ListRoomsResponse(TypedDict):
    rooms: NotRequired["aws_sdk_chime.types.room_list.RoomList"]
    """<p>The room details.</p>"""
    next_token: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoomsResponse) -> dict:
    out: dict = {}
    if "rooms" in value:
        import aws_sdk_chime.types.room_list

        out["Rooms"] = aws_sdk_chime.types.room_list.serialize_json(value["rooms"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRoomsResponse:
    out: ListRoomsResponse = {}  # type: ignore[typeddict-item]
    if "Rooms" in data:
        import aws_sdk_chime.types.room_list

        out["rooms"] = aws_sdk_chime.types.room_list.deserialize_json(data["Rooms"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
