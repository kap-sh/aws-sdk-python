"""Generated from Smithy shape ``com.amazonaws.chime#UpdateRoomMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.room_membership_role


class UpdateRoomMembershipRequest(TypedDict, closed=True):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The room ID.</p>"""
    member_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The member ID.</p>"""
    role: NotRequired["aws_sdk_chime.types.room_membership_role.RoomMembershipRole"]
    """<p>The role of the member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoomMembershipRequest) -> dict:
    out: dict = {}
    if "role" in value:
        import aws_sdk_chime.types.room_membership_role

        out["Role"] = aws_sdk_chime.types.room_membership_role.serialize_json(
            value["role"]
        )
    return out


def deserialize_json(data: dict) -> UpdateRoomMembershipRequest:
    out: UpdateRoomMembershipRequest = {}  # type: ignore[typeddict-item]
    if "Role" in data:
        import aws_sdk_chime.types.room_membership_role

        out["role"] = aws_sdk_chime.types.room_membership_role.deserialize_json(
            data["Role"]
        )
    return out
