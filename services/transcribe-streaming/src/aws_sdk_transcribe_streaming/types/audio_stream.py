"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#AudioStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_transcribe_streaming.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.audio_event
    import aws_sdk_transcribe_streaming.types.configuration_event


class _AudioStream_AudioEvent(TypedDict):
    AudioEvent: "aws_sdk_transcribe_streaming.types.audio_event.AudioEvent"


class _AudioStream_ConfigurationEvent(TypedDict):
    ConfigurationEvent: (
        "aws_sdk_transcribe_streaming.types.configuration_event.ConfigurationEvent"
    )


AudioStream: TypeAlias = _AudioStream_AudioEvent | _AudioStream_ConfigurationEvent


# --- restJson1 ser/de ---
def serialize_json(value: AudioStream) -> dict:
    if "AudioEvent" in value:
        import aws_sdk_transcribe_streaming.types.audio_event

        return {
            "AudioEvent": aws_sdk_transcribe_streaming.types.audio_event.serialize_json(
                value["AudioEvent"]
            )
        }
    elif "ConfigurationEvent" in value:
        import aws_sdk_transcribe_streaming.types.configuration_event

        return {
            "ConfigurationEvent": aws_sdk_transcribe_streaming.types.configuration_event.serialize_json(
                value["ConfigurationEvent"]
            )
        }
    else:
        raise SerializationError("AudioStream: no variant present")


def deserialize_json(data: dict) -> AudioStream:
    if "AudioEvent" in data:
        import aws_sdk_transcribe_streaming.types.audio_event

        return {
            "AudioEvent": aws_sdk_transcribe_streaming.types.audio_event.deserialize_json(
                data["AudioEvent"]
            )
        }
    elif "ConfigurationEvent" in data:
        import aws_sdk_transcribe_streaming.types.configuration_event

        return {
            "ConfigurationEvent": aws_sdk_transcribe_streaming.types.configuration_event.deserialize_json(
                data["ConfigurationEvent"]
            )
        }
    else:
        raise DeserializationError("AudioStream: no recognized variant key")
