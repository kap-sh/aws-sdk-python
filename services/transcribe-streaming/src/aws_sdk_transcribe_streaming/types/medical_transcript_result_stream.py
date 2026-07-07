"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalTranscriptResultStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_transcribe_streaming._iter import AnyIterator
from aws_sdk_transcribe_streaming._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.errors.bad_request_exception
    import aws_sdk_transcribe_streaming.errors.conflict_exception
    import aws_sdk_transcribe_streaming.errors.internal_failure_exception
    import aws_sdk_transcribe_streaming.errors.limit_exceeded_exception
    import aws_sdk_transcribe_streaming.errors.service_unavailable_exception
    import aws_sdk_transcribe_streaming.types.medical_transcript_event


class _MedicalTranscriptResultStream_TranscriptEvent(TypedDict, closed=True):
    TranscriptEvent: "aws_sdk_transcribe_streaming.types.medical_transcript_event.MedicalTranscriptEvent"


class _MedicalTranscriptResultStream_BadRequestException(TypedDict, closed=True):
    BadRequestException: (
        "aws_sdk_transcribe_streaming.errors.bad_request_exception.BadRequestException_"
    )


class _MedicalTranscriptResultStream_LimitExceededException(TypedDict, closed=True):
    LimitExceededException: "aws_sdk_transcribe_streaming.errors.limit_exceeded_exception.LimitExceededException_"


class _MedicalTranscriptResultStream_InternalFailureException(TypedDict, closed=True):
    InternalFailureException: "aws_sdk_transcribe_streaming.errors.internal_failure_exception.InternalFailureException_"


class _MedicalTranscriptResultStream_ConflictException(TypedDict, closed=True):
    ConflictException: (
        "aws_sdk_transcribe_streaming.errors.conflict_exception.ConflictException_"
    )


class _MedicalTranscriptResultStream_ServiceUnavailableException(
    TypedDict, closed=True
):
    ServiceUnavailableException: "aws_sdk_transcribe_streaming.errors.service_unavailable_exception.ServiceUnavailableException_"


_MedicalTranscriptResultStream: TypeAlias = (
    _MedicalTranscriptResultStream_TranscriptEvent
    | _MedicalTranscriptResultStream_BadRequestException
    | _MedicalTranscriptResultStream_LimitExceededException
    | _MedicalTranscriptResultStream_InternalFailureException
    | _MedicalTranscriptResultStream_ConflictException
    | _MedicalTranscriptResultStream_ServiceUnavailableException
)
MedicalTranscriptResultStream: TypeAlias = AnyIterator[_MedicalTranscriptResultStream]


def serialize_event_json(value: _MedicalTranscriptResultStream) -> bytes:
    match value:
        case {"TranscriptEvent": payload}:
            import aws_sdk_transcribe_streaming.types.medical_transcript_event

            return aws_sdk_transcribe_streaming.types.medical_transcript_event.serialize_event_json(
                payload
            )
        case {"BadRequestException": payload}:
            import aws_sdk_transcribe_streaming.errors.bad_request_exception

            return aws_sdk_transcribe_streaming.errors.bad_request_exception.serialize_event_json(
                payload
            )
        case {"LimitExceededException": payload}:
            import aws_sdk_transcribe_streaming.errors.limit_exceeded_exception

            return aws_sdk_transcribe_streaming.errors.limit_exceeded_exception.serialize_event_json(
                payload
            )
        case {"InternalFailureException": payload}:
            import aws_sdk_transcribe_streaming.errors.internal_failure_exception

            return aws_sdk_transcribe_streaming.errors.internal_failure_exception.serialize_event_json(
                payload
            )
        case {"ConflictException": payload}:
            import aws_sdk_transcribe_streaming.errors.conflict_exception

            return aws_sdk_transcribe_streaming.errors.conflict_exception.serialize_event_json(
                payload
            )
        case {"ServiceUnavailableException": payload}:
            import aws_sdk_transcribe_streaming.errors.service_unavailable_exception

            return aws_sdk_transcribe_streaming.errors.service_unavailable_exception.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"MedicalTranscriptResultStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _MedicalTranscriptResultStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "BadRequestException":
                import aws_sdk_transcribe_streaming.errors.bad_request_exception

                raise aws_sdk_transcribe_streaming.errors.bad_request_exception.BadRequestException(
                    aws_sdk_transcribe_streaming.errors.bad_request_exception.deserialize_event_json(
                        message
                    )
                )
            case "LimitExceededException":
                import aws_sdk_transcribe_streaming.errors.limit_exceeded_exception

                raise aws_sdk_transcribe_streaming.errors.limit_exceeded_exception.LimitExceededException(
                    aws_sdk_transcribe_streaming.errors.limit_exceeded_exception.deserialize_event_json(
                        message
                    )
                )
            case "InternalFailureException":
                import aws_sdk_transcribe_streaming.errors.internal_failure_exception

                raise aws_sdk_transcribe_streaming.errors.internal_failure_exception.InternalFailureException(
                    aws_sdk_transcribe_streaming.errors.internal_failure_exception.deserialize_event_json(
                        message
                    )
                )
            case "ConflictException":
                import aws_sdk_transcribe_streaming.errors.conflict_exception

                raise aws_sdk_transcribe_streaming.errors.conflict_exception.ConflictException(
                    aws_sdk_transcribe_streaming.errors.conflict_exception.deserialize_event_json(
                        message
                    )
                )
            case "ServiceUnavailableException":
                import aws_sdk_transcribe_streaming.errors.service_unavailable_exception

                raise aws_sdk_transcribe_streaming.errors.service_unavailable_exception.ServiceUnavailableException(
                    aws_sdk_transcribe_streaming.errors.service_unavailable_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(
            f"MedicalTranscriptResultStream: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "TranscriptEvent":
            import aws_sdk_transcribe_streaming.types.medical_transcript_event

            return {
                "TranscriptEvent": aws_sdk_transcribe_streaming.types.medical_transcript_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"MedicalTranscriptResultStream: unrecognized event-type {event_type!r}"
            )
