"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#CallAnalyticsTranscriptResultStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_transcribe_streaming.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.errors.bad_request_exception
    import aws_sdk_transcribe_streaming.errors.conflict_exception
    import aws_sdk_transcribe_streaming.errors.internal_failure_exception
    import aws_sdk_transcribe_streaming.errors.limit_exceeded_exception
    import aws_sdk_transcribe_streaming.errors.service_unavailable_exception
    import aws_sdk_transcribe_streaming.types.category_event
    import aws_sdk_transcribe_streaming.types.utterance_event


class _CallAnalyticsTranscriptResultStream_UtteranceEvent(TypedDict):
    UtteranceEvent: "aws_sdk_transcribe_streaming.types.utterance_event.UtteranceEvent"


class _CallAnalyticsTranscriptResultStream_CategoryEvent(TypedDict):
    CategoryEvent: "aws_sdk_transcribe_streaming.types.category_event.CategoryEvent"


class _CallAnalyticsTranscriptResultStream_BadRequestException(TypedDict):
    BadRequestException: (
        "aws_sdk_transcribe_streaming.errors.bad_request_exception.BadRequestException"
    )


class _CallAnalyticsTranscriptResultStream_LimitExceededException(TypedDict):
    LimitExceededException: "aws_sdk_transcribe_streaming.errors.limit_exceeded_exception.LimitExceededException"


class _CallAnalyticsTranscriptResultStream_InternalFailureException(TypedDict):
    InternalFailureException: "aws_sdk_transcribe_streaming.errors.internal_failure_exception.InternalFailureException"


class _CallAnalyticsTranscriptResultStream_ConflictException(TypedDict):
    ConflictException: (
        "aws_sdk_transcribe_streaming.errors.conflict_exception.ConflictException"
    )


class _CallAnalyticsTranscriptResultStream_ServiceUnavailableException(TypedDict):
    ServiceUnavailableException: "aws_sdk_transcribe_streaming.errors.service_unavailable_exception.ServiceUnavailableException"


CallAnalyticsTranscriptResultStream: TypeAlias = (
    _CallAnalyticsTranscriptResultStream_UtteranceEvent
    | _CallAnalyticsTranscriptResultStream_CategoryEvent
    | _CallAnalyticsTranscriptResultStream_BadRequestException
    | _CallAnalyticsTranscriptResultStream_LimitExceededException
    | _CallAnalyticsTranscriptResultStream_InternalFailureException
    | _CallAnalyticsTranscriptResultStream_ConflictException
    | _CallAnalyticsTranscriptResultStream_ServiceUnavailableException
)


# --- restJson1 ser/de ---
def serialize_json(value: CallAnalyticsTranscriptResultStream) -> dict:
    if "UtteranceEvent" in value:
        import aws_sdk_transcribe_streaming.types.utterance_event

        return {
            "UtteranceEvent": aws_sdk_transcribe_streaming.types.utterance_event.serialize_json(
                value["UtteranceEvent"]
            )
        }
    elif "CategoryEvent" in value:
        import aws_sdk_transcribe_streaming.types.category_event

        return {
            "CategoryEvent": aws_sdk_transcribe_streaming.types.category_event.serialize_json(
                value["CategoryEvent"]
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
        raise SerializationError(
            "CallAnalyticsTranscriptResultStream: no variant present"
        )


def deserialize_json(data: dict) -> CallAnalyticsTranscriptResultStream:
    if "UtteranceEvent" in data:
        import aws_sdk_transcribe_streaming.types.utterance_event

        return {
            "UtteranceEvent": aws_sdk_transcribe_streaming.types.utterance_event.deserialize_json(
                data["UtteranceEvent"]
            )
        }
    elif "CategoryEvent" in data:
        import aws_sdk_transcribe_streaming.types.category_event

        return {
            "CategoryEvent": aws_sdk_transcribe_streaming.types.category_event.deserialize_json(
                data["CategoryEvent"]
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
            "CallAnalyticsTranscriptResultStream: no recognized variant key"
        )
