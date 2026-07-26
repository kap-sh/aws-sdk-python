"""Generated from Smithy shape ``com.amazonaws.chime#CreateRoomMembershipResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.room_membership


class CreateRoomMembershipResponse(TypedDict, closed=True):
    room_membership: NotRequired["capo_chime.types.room_membership.RoomMembership"]
    """<p>The room membership details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoomMembershipResponse) -> dict:
    out: dict = {}
    if "room_membership" in value:
        import capo_chime.types.room_membership

        out["RoomMembership"] = capo_chime.types.room_membership.serialize_json(
            value["room_membership"]
        )
    return out


def deserialize_json(data: dict) -> CreateRoomMembershipResponse:
    out: CreateRoomMembershipResponse = {}  # type: ignore[typeddict-item]
    if "RoomMembership" in data:
        import capo_chime.types.room_membership

        out["room_membership"] = capo_chime.types.room_membership.deserialize_json(
            data["RoomMembership"]
        )
    return out
