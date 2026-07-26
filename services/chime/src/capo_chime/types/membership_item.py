"""Generated from Smithy shape ``com.amazonaws.chime#MembershipItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string
    import capo_chime.types.room_membership_role


class MembershipItem(TypedDict, closed=True):
    member_id: NotRequired["capo_chime.types.non_empty_string.NonEmptyString"]
    """<p>The member ID.</p>"""
    role: NotRequired["capo_chime.types.room_membership_role.RoomMembershipRole"]
    """<p>The member role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipItem) -> dict:
    out: dict = {}
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    if "role" in value:
        import capo_chime.types.room_membership_role

        out["Role"] = capo_chime.types.room_membership_role.serialize_json(
            value["role"]
        )
    return out


def deserialize_json(data: dict) -> MembershipItem:
    out: MembershipItem = {}  # type: ignore[typeddict-item]
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    if "Role" in data:
        import capo_chime.types.room_membership_role

        out["role"] = capo_chime.types.room_membership_role.deserialize_json(
            data["Role"]
        )
    return out
