"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeInputStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connecthealth._iter import AnyIterator
from aws_sdk_connecthealth._protocol.eventstream import Message

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


_MedicalScribeInputStream: TypeAlias = (
    _MedicalScribeInputStream_audioEvent
    | _MedicalScribeInputStream_binaryAudioEvent
    | _MedicalScribeInputStream_sessionControlEvent
    | _MedicalScribeInputStream_configurationEvent
)
MedicalScribeInputStream: TypeAlias = AnyIterator[_MedicalScribeInputStream]


def serialize_event_json(value: _MedicalScribeInputStream) -> bytes:
    match value:
        case {"audioEvent": payload}:
            import aws_sdk_connecthealth.types.medical_scribe_audio_event

            return aws_sdk_connecthealth.types.medical_scribe_audio_event.serialize_event_json(
                payload
            )
        case {"binaryAudioEvent": payload}:
            import aws_sdk_connecthealth.types.medical_scribe_binary_audio_event

            return aws_sdk_connecthealth.types.medical_scribe_binary_audio_event.serialize_event_json(
                payload
            )
        case {"sessionControlEvent": payload}:
            import aws_sdk_connecthealth.types.medical_scribe_session_control_event

            return aws_sdk_connecthealth.types.medical_scribe_session_control_event.serialize_event_json(
                payload
            )
        case {"configurationEvent": payload}:
            import aws_sdk_connecthealth.types.medical_scribe_configuration_event

            return aws_sdk_connecthealth.types.medical_scribe_configuration_event.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"MedicalScribeInputStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _MedicalScribeInputStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    event_type = headers.get(":event-type")
    match event_type:
        case "audioEvent":
            import aws_sdk_connecthealth.types.medical_scribe_audio_event

            return {
                "audioEvent": aws_sdk_connecthealth.types.medical_scribe_audio_event.deserialize_event_json(
                    message
                )
            }
        case "binaryAudioEvent":
            import aws_sdk_connecthealth.types.medical_scribe_binary_audio_event

            return {
                "binaryAudioEvent": aws_sdk_connecthealth.types.medical_scribe_binary_audio_event.deserialize_event_json(
                    message
                )
            }
        case "sessionControlEvent":
            import aws_sdk_connecthealth.types.medical_scribe_session_control_event

            return {
                "sessionControlEvent": aws_sdk_connecthealth.types.medical_scribe_session_control_event.deserialize_event_json(
                    message
                )
            }
        case "configurationEvent":
            import aws_sdk_connecthealth.types.medical_scribe_configuration_event

            return {
                "configurationEvent": aws_sdk_connecthealth.types.medical_scribe_configuration_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"MedicalScribeInputStream: unrecognized event-type {event_type!r}"
            )
