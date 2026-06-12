"""Generated from Smithy shape ``com.amazonaws.chime#DeleteRoomMembershipRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string


class DeleteRoomMembershipRequest(TypedDict):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The room ID.</p>"""
    member_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The member ID (user ID or bot ID).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRoomMembershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRoomMembershipRequest:
    out: DeleteRoomMembershipRequest = {}  # type: ignore[typeddict-item]
    return out
