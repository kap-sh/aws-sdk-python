"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeAudioEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connecthealth._protocol.eventstream import HeaderValue, Message
from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.audio_chunk


class MedicalScribeAudioEvent(TypedDict, closed=True):
    audio_chunk: "aws_sdk_connecthealth.types.audio_chunk.AudioChunk"
    """<p>The audio data chunk</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeAudioEvent) -> dict:
    out: dict = {}
    import aws_sdk_connecthealth.types.audio_chunk

    out["audioChunk"] = aws_sdk_connecthealth.types.audio_chunk.serialize_json(
        value["audio_chunk"]
    )
    return out


def deserialize_json(data: dict) -> MedicalScribeAudioEvent:
    out: MedicalScribeAudioEvent = {}  # type: ignore[typeddict-item]
    if "audioChunk" in data:
        import aws_sdk_connecthealth.types.audio_chunk

        out["audio_chunk"] = aws_sdk_connecthealth.types.audio_chunk.deserialize_json(
            data["audioChunk"]
        )
    else:
        raise DeserializationError("MedicalScribeAudioEvent.audio_chunk required")
    return out


def serialize_event_json(value: MedicalScribeAudioEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "audioEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MedicalScribeAudioEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MedicalScribeAudioEvent = {}  # type: ignore[typeddict-item]
    return out
