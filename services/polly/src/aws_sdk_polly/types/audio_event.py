"""Generated from Smithy shape ``com.amazonaws.polly#AudioEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_polly._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_polly.types.audio_chunk


class AudioEvent(TypedDict, closed=True):
    audio_chunk: NotRequired["aws_sdk_polly.types.audio_chunk.AudioChunk"]
    """<p>A chunk of synthesized audio data encoded in the format specified by the <code>OutputFormat</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioEvent) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AudioEvent:
    out: AudioEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_json(value: AudioEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "AudioEvent"}
    payload = b""
    payload = value["audio_chunk"]
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AudioEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AudioEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out["audio_chunk"] = payload
    return out
