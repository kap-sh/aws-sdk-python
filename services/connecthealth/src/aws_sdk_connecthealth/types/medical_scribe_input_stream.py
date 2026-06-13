"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeInputStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connecthealth.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.medical_scribe_audio_event
    import aws_sdk_connecthealth.types.medical_scribe_binary_audio_event
    import aws_sdk_connecthealth.types.medical_scribe_configuration_event
    import aws_sdk_connecthealth.types.medical_scribe_session_control_event


class _MedicalScribeInputStream_audioEvent(TypedDict):
    audioEvent: (
        "aws_sdk_connecthealth.types.medical_scribe_audio_event.MedicalScribeAudioEvent"
    )


class _MedicalScribeInputStream_binaryAudioEvent(TypedDict):
    binaryAudioEvent: "aws_sdk_connecthealth.types.medical_scribe_binary_audio_event.MedicalScribeBinaryAudioEvent"


class _MedicalScribeInputStream_sessionControlEvent(TypedDict):
    sessionControlEvent: "aws_sdk_connecthealth.types.medical_scribe_session_control_event.MedicalScribeSessionControlEvent"


class _MedicalScribeInputStream_configurationEvent(TypedDict):
    configurationEvent: "aws_sdk_connecthealth.types.medical_scribe_configuration_event.MedicalScribeConfigurationEvent"


MedicalScribeInputStream: TypeAlias = (
    _MedicalScribeInputStream_audioEvent
    | _MedicalScribeInputStream_binaryAudioEvent
    | _MedicalScribeInputStream_sessionControlEvent
    | _MedicalScribeInputStream_configurationEvent
)


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeInputStream) -> dict:
    if "audioEvent" in value:
        import aws_sdk_connecthealth.types.medical_scribe_audio_event

        return {
            "audioEvent": aws_sdk_connecthealth.types.medical_scribe_audio_event.serialize_json(
                value["audioEvent"]
            )
        }
    elif "binaryAudioEvent" in value:
        import aws_sdk_connecthealth.types.medical_scribe_binary_audio_event

        return {
            "binaryAudioEvent": aws_sdk_connecthealth.types.medical_scribe_binary_audio_event.serialize_json(
                value["binaryAudioEvent"]
            )
        }
    elif "sessionControlEvent" in value:
        import aws_sdk_connecthealth.types.medical_scribe_session_control_event

        return {
            "sessionControlEvent": aws_sdk_connecthealth.types.medical_scribe_session_control_event.serialize_json(
                value["sessionControlEvent"]
            )
        }
    elif "configurationEvent" in value:
        import aws_sdk_connecthealth.types.medical_scribe_configuration_event

        return {
            "configurationEvent": aws_sdk_connecthealth.types.medical_scribe_configuration_event.serialize_json(
                value["configurationEvent"]
            )
        }
    else:
        raise SerializationError("MedicalScribeInputStream: no variant present")


def deserialize_json(data: dict) -> MedicalScribeInputStream:
    if "audioEvent" in data:
        import aws_sdk_connecthealth.types.medical_scribe_audio_event

        return {
            "audioEvent": aws_sdk_connecthealth.types.medical_scribe_audio_event.deserialize_json(
                data["audioEvent"]
            )
        }
    elif "binaryAudioEvent" in data:
        import aws_sdk_connecthealth.types.medical_scribe_binary_audio_event

        return {
            "binaryAudioEvent": aws_sdk_connecthealth.types.medical_scribe_binary_audio_event.deserialize_json(
                data["binaryAudioEvent"]
            )
        }
    elif "sessionControlEvent" in data:
        import aws_sdk_connecthealth.types.medical_scribe_session_control_event

        return {
            "sessionControlEvent": aws_sdk_connecthealth.types.medical_scribe_session_control_event.deserialize_json(
                data["sessionControlEvent"]
            )
        }
    elif "configurationEvent" in data:
        import aws_sdk_connecthealth.types.medical_scribe_configuration_event

        return {
            "configurationEvent": aws_sdk_connecthealth.types.medical_scribe_configuration_event.deserialize_json(
                data["configurationEvent"]
            )
        }
    else:
        raise DeserializationError(
            "MedicalScribeInputStream: no recognized variant key"
        )
