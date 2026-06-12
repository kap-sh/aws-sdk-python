"""Generated from Smithy shape ``com.amazonaws.chime#DeleteRoomRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string


class DeleteRoomRequest(TypedDict):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The chat room ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRoomRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRoomRequest:
    out: DeleteRoomRequest = {}  # type: ignore[typeddict-item]
    return out
