"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#IssueDetected``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.character_offsets


class IssueDetected(TypedDict, closed=True):
    character_offsets: NotRequired[
        "aws_sdk_transcribe_streaming.types.character_offsets.CharacterOffsets"
    ]
    """<p>Provides the timestamps that identify when in an audio segment the specified issue occurs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IssueDetected) -> dict:
    out: dict = {}
    if "character_offsets" in value:
        import aws_sdk_transcribe_streaming.types.character_offsets

        out["CharacterOffsets"] = (
            aws_sdk_transcribe_streaming.types.character_offsets.serialize_json(
                value["character_offsets"]
            )
        )
    return out


def deserialize_json(data: dict) -> IssueDetected:
    out: IssueDetected = {}  # type: ignore[typeddict-item]
    if "CharacterOffsets" in data:
        import aws_sdk_transcribe_streaming.types.character_offsets

        out["character_offsets"] = (
            aws_sdk_transcribe_streaming.types.character_offsets.deserialize_json(
                data["CharacterOffsets"]
            )
        )
    return out
