"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeAudioEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transcribe_streaming.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.audio_chunk


class MedicalScribeAudioEvent(TypedDict):
    audio_chunk: "aws_sdk_transcribe_streaming.types.audio_chunk.AudioChunk"
    """<p> An audio blob containing the next segment of audio from your application, with a maximum duration of 1 second. The maximum size in bytes varies based on audio properties. </p> <p>Find recommended size in <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#best-practices\">Transcribing streaming best practices</a>. </p> <p> Size calculation: <code>Duration (s) * Sample Rate (Hz) * Number of Channels * 2 (Bytes per Sample)</code> </p> <p> For example, a 1-second chunk of 16 kHz, 2-channel, 16-bit audio would be <code>1 * 16000 * 2 * 2 = 64000 bytes</code>. </p> <p> For 8 kHz, 1-channel, 16-bit audio, a 1-second chunk would be <code>1 * 8000 * 1 * 2 = 16000 bytes</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeAudioEvent) -> dict:
    out: dict = {}
    import aws_sdk_transcribe_streaming.types.audio_chunk

    out["AudioChunk"] = aws_sdk_transcribe_streaming.types.audio_chunk.serialize_json(
        value["audio_chunk"]
    )
    return out


def deserialize_json(data: dict) -> MedicalScribeAudioEvent:
    out: MedicalScribeAudioEvent = {}  # type: ignore[typeddict-item]
    if "AudioChunk" in data:
        import aws_sdk_transcribe_streaming.types.audio_chunk

        out["audio_chunk"] = (
            aws_sdk_transcribe_streaming.types.audio_chunk.deserialize_json(
                data["AudioChunk"]
            )
        )
    else:
        raise DeserializationError("MedicalScribeAudioEvent.audio_chunk required")
    return out
