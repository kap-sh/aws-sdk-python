"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeOutputStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connecthealth._iter import AnyIterator
from aws_sdk_connecthealth._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_connecthealth.errors.internal_server_exception
    import aws_sdk_connecthealth.errors.validation_exception
    import aws_sdk_connecthealth.types.medical_scribe_transcript_event


class _MedicalScribeOutputStream_transcriptEvent(TypedDict):
    transcriptEvent: "aws_sdk_connecthealth.types.medical_scribe_transcript_event.MedicalScribeTranscriptEvent"


class _MedicalScribeOutputStream_internalFailureException(TypedDict):
    internalFailureException: "aws_sdk_connecthealth.errors.internal_server_exception.InternalServerException_"


class _MedicalScribeOutputStream_validationException(TypedDict):
    validationException: (
        "aws_sdk_connecthealth.errors.validation_exception.ValidationException_"
    )


_MedicalScribeOutputStream: TypeAlias = (
    _MedicalScribeOutputStream_transcriptEvent
    | _MedicalScribeOutputStream_internalFailureException
    | _MedicalScribeOutputStream_validationException
)
MedicalScribeOutputStream: TypeAlias = AnyIterator[_MedicalScribeOutputStream]


def serialize_event_json(value: _MedicalScribeOutputStream) -> bytes:
    match value:
        case {"transcriptEvent": payload}:
            import aws_sdk_connecthealth.types.medical_scribe_transcript_event

            return aws_sdk_connecthealth.types.medical_scribe_transcript_event.serialize_event_json(
                payload
            )
        case {"internalFailureException": payload}:
            import aws_sdk_connecthealth.errors.internal_server_exception

            return aws_sdk_connecthealth.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"validationException": payload}:
            import aws_sdk_connecthealth.errors.validation_exception

            return (
                aws_sdk_connecthealth.errors.validation_exception.serialize_event_json(
                    payload
                )
            )
        case _:
            raise ValueError(
                f"MedicalScribeOutputStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _MedicalScribeOutputStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "internalFailureException":
                import aws_sdk_connecthealth.errors.internal_server_exception

                raise aws_sdk_connecthealth.errors.internal_server_exception.InternalServerException(
                    aws_sdk_connecthealth.errors.internal_server_exception.deserialize_event_json(
                        message
                    )
                )
            case "validationException":
                import aws_sdk_connecthealth.errors.validation_exception

                raise aws_sdk_connecthealth.errors.validation_exception.ValidationException(
                    aws_sdk_connecthealth.errors.validation_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(
            f"MedicalScribeOutputStream: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "transcriptEvent":
            import aws_sdk_connecthealth.types.medical_scribe_transcript_event

            return {
                "transcriptEvent": aws_sdk_connecthealth.types.medical_scribe_transcript_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"MedicalScribeOutputStream: unrecognized event-type {event_type!r}"
            )
