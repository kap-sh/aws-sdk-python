"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeBinaryAudioEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connecthealth._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.audio_chunk


class MedicalScribeBinaryAudioEvent(TypedDict):
    audio_chunk: "aws_sdk_connecthealth.types.audio_chunk.AudioChunk"
    """<p>The raw binary audio data chunk</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeBinaryAudioEvent) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> MedicalScribeBinaryAudioEvent:
    out: MedicalScribeBinaryAudioEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_json(value: MedicalScribeBinaryAudioEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "binaryAudioEvent"}
    payload = b""
    payload = value["audio_chunk"]
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MedicalScribeBinaryAudioEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MedicalScribeBinaryAudioEvent = {}  # type: ignore[typeddict-item]
    out["audio_chunk"] = payload
    return out
