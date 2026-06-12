"""Generated from Smithy shape ``com.amazonaws.chime#CreateRoomMembershipResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.room_membership


class CreateRoomMembershipResponse(TypedDict):
    room_membership: NotRequired["aws_sdk_chime.types.room_membership.RoomMembership"]
    """<p>The room membership details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoomMembershipResponse) -> dict:
    out: dict = {}
    if "room_membership" in value:
        import aws_sdk_chime.types.room_membership

        out["RoomMembership"] = aws_sdk_chime.types.room_membership.serialize_json(
            value["room_membership"]
        )
    return out


def deserialize_json(data: dict) -> CreateRoomMembershipResponse:
    out: CreateRoomMembershipResponse = {}  # type: ignore[typeddict-item]
    if "RoomMembership" in data:
        import aws_sdk_chime.types.room_membership

        out["room_membership"] = aws_sdk_chime.types.room_membership.deserialize_json(
            data["RoomMembership"]
        )
    return out
