"""Generated from Smithy shape ``com.amazonaws.chime#UpdateRoomMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string
    import capo_chime.types.room_membership_role


class UpdateRoomMembershipRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    room_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The room ID.</p>"""
    member_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The member ID.</p>"""
    role: NotRequired["capo_chime.types.room_membership_role.RoomMembershipRole"]
    """<p>The role of the member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoomMembershipRequest) -> dict:
    out: dict = {}
    if "role" in value:
        import capo_chime.types.room_membership_role

        out["Role"] = capo_chime.types.room_membership_role.serialize_json(
            value["role"]
        )
    return out


def deserialize_json(data: dict) -> UpdateRoomMembershipRequest:
    out: UpdateRoomMembershipRequest = {}  # type: ignore[typeddict-item]
    if "Role" in data:
        import capo_chime.types.room_membership_role

        out["role"] = capo_chime.types.room_membership_role.deserialize_json(
            data["Role"]
        )
    return out
