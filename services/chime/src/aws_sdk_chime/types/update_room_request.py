"""Generated from Smithy shape ``com.amazonaws.chime#UpdateRoomRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.sensitive_string


class UpdateRoomRequest(TypedDict, closed=True):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    room_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The room ID.</p>"""
    name: NotRequired["aws_sdk_chime.types.sensitive_string.SensitiveString"]
    """<p>The room name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoomRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateRoomRequest:
    out: UpdateRoomRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
