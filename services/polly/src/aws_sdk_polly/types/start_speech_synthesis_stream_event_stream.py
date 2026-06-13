"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisStreamEventStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_polly.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_polly.errors.service_failure_exception
    import aws_sdk_polly.errors.service_quota_exceeded_exception
    import aws_sdk_polly.errors.throttling_exception
    import aws_sdk_polly.errors.validation_exception
    import aws_sdk_polly.types.audio_event
    import aws_sdk_polly.types.stream_closed_event


class _StartSpeechSynthesisStreamEventStream_AudioEvent(TypedDict):
    AudioEvent: "aws_sdk_polly.types.audio_event.AudioEvent"


class _StartSpeechSynthesisStreamEventStream_StreamClosedEvent(TypedDict):
    StreamClosedEvent: "aws_sdk_polly.types.stream_closed_event.StreamClosedEvent"


class _StartSpeechSynthesisStreamEventStream_ValidationException(TypedDict):
    ValidationException: (
        "aws_sdk_polly.errors.validation_exception.ValidationException_"
    )


class _StartSpeechSynthesisStreamEventStream_ServiceQuotaExceededException(TypedDict):
    ServiceQuotaExceededException: "aws_sdk_polly.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _StartSpeechSynthesisStreamEventStream_ServiceFailureException(TypedDict):
    ServiceFailureException: (
        "aws_sdk_polly.errors.service_failure_exception.ServiceFailureException_"
    )


class _StartSpeechSynthesisStreamEventStream_ThrottlingException(TypedDict):
    ThrottlingException: (
        "aws_sdk_polly.errors.throttling_exception.ThrottlingException_"
    )


StartSpeechSynthesisStreamEventStream: TypeAlias = (
    _StartSpeechSynthesisStreamEventStream_AudioEvent
    | _StartSpeechSynthesisStreamEventStream_StreamClosedEvent
    | _StartSpeechSynthesisStreamEventStream_ValidationException
    | _StartSpeechSynthesisStreamEventStream_ServiceQuotaExceededException
    | _StartSpeechSynthesisStreamEventStream_ServiceFailureException
    | _StartSpeechSynthesisStreamEventStream_ThrottlingException
)


# --- restJson1 ser/de ---
def serialize_json(value: StartSpeechSynthesisStreamEventStream) -> dict:
    if "AudioEvent" in value:
        import aws_sdk_polly.types.audio_event

        return {
            "AudioEvent": aws_sdk_polly.types.audio_event.serialize_json(
                value["AudioEvent"]
            )
        }
    elif "StreamClosedEvent" in value:
        import aws_sdk_polly.types.stream_closed_event

        return {
            "StreamClosedEvent": aws_sdk_polly.types.stream_closed_event.serialize_json(
                value["StreamClosedEvent"]
            )
        }
    elif "ValidationException" in value:
        import aws_sdk_polly.errors.validation_exception

        return {
            "ValidationException": aws_sdk_polly.errors.validation_exception.serialize_json(
                value["ValidationException"]
            )
        }
    elif "ServiceQuotaExceededException" in value:
        import aws_sdk_polly.errors.service_quota_exceeded_exception

        return {
            "ServiceQuotaExceededException": aws_sdk_polly.errors.service_quota_exceeded_exception.serialize_json(
                value["ServiceQuotaExceededException"]
            )
        }
    elif "ServiceFailureException" in value:
        import aws_sdk_polly.errors.service_failure_exception

        return {
            "ServiceFailureException": aws_sdk_polly.errors.service_failure_exception.serialize_json(
                value["ServiceFailureException"]
            )
        }
    elif "ThrottlingException" in value:
        import aws_sdk_polly.errors.throttling_exception

        return {
            "ThrottlingException": aws_sdk_polly.errors.throttling_exception.serialize_json(
                value["ThrottlingException"]
            )
        }
    else:
        raise SerializationError(
            "StartSpeechSynthesisStreamEventStream: no variant present"
        )


def deserialize_json(data: dict) -> StartSpeechSynthesisStreamEventStream:
    if "AudioEvent" in data:
        import aws_sdk_polly.types.audio_event

        return {
            "AudioEvent": aws_sdk_polly.types.audio_event.deserialize_json(
                data["AudioEvent"]
            )
        }
    elif "StreamClosedEvent" in data:
        import aws_sdk_polly.types.stream_closed_event

        return {
            "StreamClosedEvent": aws_sdk_polly.types.stream_closed_event.deserialize_json(
                data["StreamClosedEvent"]
            )
        }
    elif "ValidationException" in data:
        import aws_sdk_polly.errors.validation_exception

        return {
            "ValidationException": aws_sdk_polly.errors.validation_exception.deserialize_json(
                data["ValidationException"]
            )
        }
    elif "ServiceQuotaExceededException" in data:
        import aws_sdk_polly.errors.service_quota_exceeded_exception

        return {
            "ServiceQuotaExceededException": aws_sdk_polly.errors.service_quota_exceeded_exception.deserialize_json(
                data["ServiceQuotaExceededException"]
            )
        }
    elif "ServiceFailureException" in data:
        import aws_sdk_polly.errors.service_failure_exception

        return {
            "ServiceFailureException": aws_sdk_polly.errors.service_failure_exception.deserialize_json(
                data["ServiceFailureException"]
            )
        }
    elif "ThrottlingException" in data:
        import aws_sdk_polly.errors.throttling_exception

        return {
            "ThrottlingException": aws_sdk_polly.errors.throttling_exception.deserialize_json(
                data["ThrottlingException"]
            )
        }
    else:
        raise DeserializationError(
            "StartSpeechSynthesisStreamEventStream: no recognized variant key"
        )
