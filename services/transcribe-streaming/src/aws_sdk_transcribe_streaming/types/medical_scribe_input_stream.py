"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeInputStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_transcribe_streaming.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.medical_scribe_audio_event
    import aws_sdk_transcribe_streaming.types.medical_scribe_configuration_event
    import aws_sdk_transcribe_streaming.types.medical_scribe_session_control_event


class _MedicalScribeInputStream_AudioEvent(TypedDict):
    AudioEvent: "aws_sdk_transcribe_streaming.types.medical_scribe_audio_event.MedicalScribeAudioEvent"


class _MedicalScribeInputStream_SessionControlEvent(TypedDict):
    SessionControlEvent: "aws_sdk_transcribe_streaming.types.medical_scribe_session_control_event.MedicalScribeSessionControlEvent"


class _MedicalScribeInputStream_ConfigurationEvent(TypedDict):
    ConfigurationEvent: "aws_sdk_transcribe_streaming.types.medical_scribe_configuration_event.MedicalScribeConfigurationEvent"


MedicalScribeInputStream: TypeAlias = (
    _MedicalScribeInputStream_AudioEvent
    | _MedicalScribeInputStream_SessionControlEvent
    | _MedicalScribeInputStream_ConfigurationEvent
)


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeInputStream) -> dict:
    if "AudioEvent" in value:
        import aws_sdk_transcribe_streaming.types.medical_scribe_audio_event

        return {
            "AudioEvent": aws_sdk_transcribe_streaming.types.medical_scribe_audio_event.serialize_json(
                value["AudioEvent"]
            )
        }
    elif "SessionControlEvent" in value:
        import aws_sdk_transcribe_streaming.types.medical_scribe_session_control_event

        return {
            "SessionControlEvent": aws_sdk_transcribe_streaming.types.medical_scribe_session_control_event.serialize_json(
                value["SessionControlEvent"]
            )
        }
    elif "ConfigurationEvent" in value:
        import aws_sdk_transcribe_streaming.types.medical_scribe_configuration_event

        return {
            "ConfigurationEvent": aws_sdk_transcribe_streaming.types.medical_scribe_configuration_event.serialize_json(
                value["ConfigurationEvent"]
            )
        }
    else:
        raise SerializationError("MedicalScribeInputStream: no variant present")


def deserialize_json(data: dict) -> MedicalScribeInputStream:
    if "AudioEvent" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_audio_event

        return {
            "AudioEvent": aws_sdk_transcribe_streaming.types.medical_scribe_audio_event.deserialize_json(
                data["AudioEvent"]
            )
        }
    elif "SessionControlEvent" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_session_control_event

        return {
            "SessionControlEvent": aws_sdk_transcribe_streaming.types.medical_scribe_session_control_event.deserialize_json(
                data["SessionControlEvent"]
            )
        }
    elif "ConfigurationEvent" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_configuration_event

        return {
            "ConfigurationEvent": aws_sdk_transcribe_streaming.types.medical_scribe_configuration_event.deserialize_json(
                data["ConfigurationEvent"]
            )
        }
    else:
        raise DeserializationError(
            "MedicalScribeInputStream: no recognized variant key"
        )
