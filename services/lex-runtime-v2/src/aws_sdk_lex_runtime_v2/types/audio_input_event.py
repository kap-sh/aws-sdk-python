"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#AudioInputEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_runtime_v2._protocol.eventstream import HeaderValue, Message
from aws_sdk_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.audio_chunk
    import aws_sdk_lex_runtime_v2.types.epoch_millis
    import aws_sdk_lex_runtime_v2.types.event_id
    import aws_sdk_lex_runtime_v2.types.non_empty_string


class AudioInputEvent(TypedDict):
    audio_chunk: NotRequired["aws_sdk_lex_runtime_v2.types.audio_chunk.AudioChunk"]
    """<p>An encoded stream of audio.</p>"""
    content_type: "aws_sdk_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    """<p>The encoding used for the audio chunk. You must use 8 KHz PCM 16-bit mono-channel little-endian format. The value of the field should be:</p> <p> <code>audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false</code> </p>"""
    event_id: NotRequired["aws_sdk_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier that your application assigns to the event. You can use this to identify events in logs.</p>"""
    client_timestamp_millis: "aws_sdk_lex_runtime_v2.types.epoch_millis.EpochMillis"
    """<p>A timestamp set by the client of the date and time that the event was sent to Amazon Lex V2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioInputEvent) -> dict:
    out: dict = {}
    if "audio_chunk" in value:
        import aws_sdk_lex_runtime_v2.types.audio_chunk

        out["audioChunk"] = aws_sdk_lex_runtime_v2.types.audio_chunk.serialize_json(
            value["audio_chunk"]
        )
    out["contentType"] = value["content_type"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    out["clientTimestampMillis"] = value.get("client_timestamp_millis", 0)
    return out


def deserialize_json(data: dict) -> AudioInputEvent:
    out: AudioInputEvent = {}  # type: ignore[typeddict-item]
    if "audioChunk" in data:
        import aws_sdk_lex_runtime_v2.types.audio_chunk

        out["audio_chunk"] = aws_sdk_lex_runtime_v2.types.audio_chunk.deserialize_json(
            data["audioChunk"]
        )
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("AudioInputEvent.content_type required")
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    if "clientTimestampMillis" in data:
        out["client_timestamp_millis"] = data["clientTimestampMillis"]
    else:
        out["client_timestamp_millis"] = 0
    return out


def serialize_event_json(value: AudioInputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "AudioInputEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AudioInputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AudioInputEvent = {}  # type: ignore[typeddict-item]
    return out
