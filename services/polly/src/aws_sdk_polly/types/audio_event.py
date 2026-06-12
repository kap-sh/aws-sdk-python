"""Generated from Smithy shape ``com.amazonaws.polly#AudioEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_polly.types.audio_chunk


class AudioEvent(TypedDict):
    audio_chunk: NotRequired["aws_sdk_polly.types.audio_chunk.AudioChunk"]
    """<p>A chunk of synthesized audio data encoded in the format specified by the <code>OutputFormat</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioEvent) -> dict:
    out: dict = {}
    if "audio_chunk" in value:
        import aws_sdk_polly.types.audio_chunk

        out["AudioChunk"] = aws_sdk_polly.types.audio_chunk.serialize_json(
            value["audio_chunk"]
        )
    return out


def deserialize_json(data: dict) -> AudioEvent:
    out: AudioEvent = {}  # type: ignore[typeddict-item]
    if "AudioChunk" in data:
        import aws_sdk_polly.types.audio_chunk

        out["audio_chunk"] = aws_sdk_polly.types.audio_chunk.deserialize_json(
            data["AudioChunk"]
        )
    return out
