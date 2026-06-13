"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalTranscriptResultStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_transcribe_streaming.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.errors.bad_request_exception
    import aws_sdk_transcribe_streaming.errors.conflict_exception
    import aws_sdk_transcribe_streaming.errors.internal_failure_exception
    import aws_sdk_transcribe_streaming.errors.limit_exceeded_exception
    import aws_sdk_transcribe_streaming.errors.service_unavailable_exception
    import aws_sdk_transcribe_streaming.types.medical_transcript_event


class _MedicalTranscriptResultStream_TranscriptEvent(TypedDict):
    TranscriptEvent: "aws_sdk_transcribe_streaming.types.medical_transcript_event.MedicalTranscriptEvent"


class _MedicalTranscriptResultStream_BadRequestException(TypedDict):
    BadRequestException: (
        "aws_sdk_transcribe_streaming.errors.bad_request_exception.BadRequestException_"
    )


class _MedicalTranscriptResultStream_LimitExceededException(TypedDict):
    LimitExceededException: "aws_sdk_transcribe_streaming.errors.limit_exceeded_exception.LimitExceededException_"


class _MedicalTranscriptResultStream_InternalFailureException(TypedDict):
    InternalFailureException: "aws_sdk_transcribe_streaming.errors.internal_failure_exception.InternalFailureException_"


class _MedicalTranscriptResultStream_ConflictException(TypedDict):
    ConflictException: (
        "aws_sdk_transcribe_streaming.errors.conflict_exception.ConflictException_"
    )


class _MedicalTranscriptResultStream_ServiceUnavailableException(TypedDict):
    ServiceUnavailableException: "aws_sdk_transcribe_streaming.errors.service_unavailable_exception.ServiceUnavailableException_"


MedicalTranscriptResultStream: TypeAlias = (
    _MedicalTranscriptResultStream_TranscriptEvent
    | _MedicalTranscriptResultStream_BadRequestException
    | _MedicalTranscriptResultStream_LimitExceededException
    | _MedicalTranscriptResultStream_InternalFailureException
    | _MedicalTranscriptResultStream_ConflictException
    | _MedicalTranscriptResultStream_ServiceUnavailableException
)


# --- restJson1 ser/de ---
def serialize_json(value: MedicalTranscriptResultStream) -> dict:
    if "TranscriptEvent" in value:
        import aws_sdk_transcribe_streaming.types.medical_transcript_event

        return {
            "TranscriptEvent": aws_sdk_transcribe_streaming.types.medical_transcript_event.serialize_json(
                value["TranscriptEvent"]
            )
        }
    elif "BadRequestException" in value:
        import aws_sdk_transcribe_streaming.errors.bad_request_exception

        return {
            "BadRequestException": aws_sdk_transcribe_streaming.errors.bad_request_exception.serialize_json(
                value["BadRequestException"]
            )
        }
    elif "LimitExceededException" in value:
        import aws_sdk_transcribe_streaming.errors.limit_exceeded_exception

        return {
            "LimitExceededException": aws_sdk_transcribe_streaming.errors.limit_exceeded_exception.serialize_json(
                value["LimitExceededException"]
            )
        }
    elif "InternalFailureException" in value:
        import aws_sdk_transcribe_streaming.errors.internal_failure_exception

        return {
            "InternalFailureException": aws_sdk_transcribe_streaming.errors.internal_failure_exception.serialize_json(
                value["InternalFailureException"]
            )
        }
    elif "ConflictException" in value:
        import aws_sdk_transcribe_streaming.errors.conflict_exception

        return {
            "ConflictException": aws_sdk_transcribe_streaming.errors.conflict_exception.serialize_json(
                value["ConflictException"]
            )
        }
    elif "ServiceUnavailableException" in value:
        import aws_sdk_transcribe_streaming.errors.service_unavailable_exception

        return {
            "ServiceUnavailableException": aws_sdk_transcribe_streaming.errors.service_unavailable_exception.serialize_json(
                value["ServiceUnavailableException"]
            )
        }
    else:
        raise SerializationError("MedicalTranscriptResultStream: no variant present")


def deserialize_json(data: dict) -> MedicalTranscriptResultStream:
    if "TranscriptEvent" in data:
        import aws_sdk_transcribe_streaming.types.medical_transcript_event

        return {
            "TranscriptEvent": aws_sdk_transcribe_streaming.types.medical_transcript_event.deserialize_json(
                data["TranscriptEvent"]
            )
        }
    elif "BadRequestException" in data:
        import aws_sdk_transcribe_streaming.errors.bad_request_exception

        return {
            "BadRequestException": aws_sdk_transcribe_streaming.errors.bad_request_exception.deserialize_json(
                data["BadRequestException"]
            )
        }
    elif "LimitExceededException" in data:
        import aws_sdk_transcribe_streaming.errors.limit_exceeded_exception

        return {
            "LimitExceededException": aws_sdk_transcribe_streaming.errors.limit_exceeded_exception.deserialize_json(
                data["LimitExceededException"]
            )
        }
    elif "InternalFailureException" in data:
        import aws_sdk_transcribe_streaming.errors.internal_failure_exception

        return {
            "InternalFailureException": aws_sdk_transcribe_streaming.errors.internal_failure_exception.deserialize_json(
                data["InternalFailureException"]
            )
        }
    elif "ConflictException" in data:
        import aws_sdk_transcribe_streaming.errors.conflict_exception

        return {
            "ConflictException": aws_sdk_transcribe_streaming.errors.conflict_exception.deserialize_json(
                data["ConflictException"]
            )
        }
    elif "ServiceUnavailableException" in data:
        import aws_sdk_transcribe_streaming.errors.service_unavailable_exception

        return {
            "ServiceUnavailableException": aws_sdk_transcribe_streaming.errors.service_unavailable_exception.deserialize_json(
                data["ServiceUnavailableException"]
            )
        }
    else:
        raise DeserializationError(
            "MedicalTranscriptResultStream: no recognized variant key"
        )
