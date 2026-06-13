"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeBinaryAudioEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.audio_chunk


class MedicalScribeBinaryAudioEvent(TypedDict):
    audio_chunk: "aws_sdk_connecthealth.types.audio_chunk.AudioChunk"
    """<p>The raw binary audio data chunk</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeBinaryAudioEvent) -> dict:
    out: dict = {}
    import aws_sdk_connecthealth.types.audio_chunk

    out["audioChunk"] = aws_sdk_connecthealth.types.audio_chunk.serialize_json(
        value["audio_chunk"]
    )
    return out


def deserialize_json(data: dict) -> MedicalScribeBinaryAudioEvent:
    out: MedicalScribeBinaryAudioEvent = {}  # type: ignore[typeddict-item]
    if "audioChunk" in data:
        import aws_sdk_connecthealth.types.audio_chunk

        out["audio_chunk"] = aws_sdk_connecthealth.types.audio_chunk.deserialize_json(
            data["audioChunk"]
        )
    else:
        raise DeserializationError("MedicalScribeBinaryAudioEvent.audio_chunk required")
    return out
