"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#AudioResponseEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_runtime_v2._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.audio_chunk
    import aws_sdk_lex_runtime_v2.types.event_id
    import aws_sdk_lex_runtime_v2.types.non_empty_string


class AudioResponseEvent(TypedDict):
    audio_chunk: NotRequired["aws_sdk_lex_runtime_v2.types.audio_chunk.AudioChunk"]
    """<p>A chunk of the audio to play. </p>"""
    content_type: NotRequired[
        "aws_sdk_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The encoding of the audio chunk. This is the same as the encoding configure in the <code>contentType</code> field of the <code>ConfigurationEvent</code>.</p>"""
    event_id: NotRequired["aws_sdk_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier of the event sent by Amazon Lex V2. The identifier is in the form <code>RESPONSE-N</code>, where N is a number starting with one and incremented for each event sent by Amazon Lex V2 in the current session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioResponseEvent) -> dict:
    out: dict = {}
    if "audio_chunk" in value:
        import aws_sdk_lex_runtime_v2.types.audio_chunk

        out["audioChunk"] = aws_sdk_lex_runtime_v2.types.audio_chunk.serialize_json(
            value["audio_chunk"]
        )
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> AudioResponseEvent:
    out: AudioResponseEvent = {}  # type: ignore[typeddict-item]
    if "audioChunk" in data:
        import aws_sdk_lex_runtime_v2.types.audio_chunk

        out["audio_chunk"] = aws_sdk_lex_runtime_v2.types.audio_chunk.deserialize_json(
            data["audioChunk"]
        )
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    return out


def serialize_event_json(value: AudioResponseEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "AudioResponseEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AudioResponseEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AudioResponseEvent = {}  # type: ignore[typeddict-item]
    return out
