"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#CharacterOffsets``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect_contact_lens.types.character_offset


class CharacterOffsets(TypedDict):
    begin_offset_char: NotRequired[
        "aws_sdk_connect_contact_lens.types.character_offset.CharacterOffset"
    ]
    """<p>The beginning of the issue.</p>"""
    end_offset_char: NotRequired[
        "aws_sdk_connect_contact_lens.types.character_offset.CharacterOffset"
    ]
    """<p>The end of the issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CharacterOffsets) -> dict:
    out: dict = {}
    if "begin_offset_char" in value:
        out["BeginOffsetChar"] = value["begin_offset_char"]
    if "end_offset_char" in value:
        out["EndOffsetChar"] = value["end_offset_char"]
    return out


def deserialize_json(data: dict) -> CharacterOffsets:
    out: CharacterOffsets = {}  # type: ignore[typeddict-item]
    if "BeginOffsetChar" in data:
        out["begin_offset_char"] = data["BeginOffsetChar"]
    if "EndOffsetChar" in data:
        out["end_offset_char"] = data["EndOffsetChar"]
    return out
