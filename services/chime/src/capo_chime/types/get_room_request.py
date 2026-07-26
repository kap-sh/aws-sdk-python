"""Generated from Smithy shape ``com.amazonaws.chime#GetRoomRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string


class GetRoomRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    room_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The room ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRoomRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRoomRequest:
    out: GetRoomRequest = {}  # type: ignore[typeddict-item]
    return out
