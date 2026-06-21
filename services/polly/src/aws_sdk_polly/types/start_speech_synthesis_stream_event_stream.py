"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisStreamEventStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_polly._iter import AnyIterator
from aws_sdk_polly._protocol.eventstream import Message

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


_StartSpeechSynthesisStreamEventStream: TypeAlias = (
    _StartSpeechSynthesisStreamEventStream_AudioEvent
    | _StartSpeechSynthesisStreamEventStream_StreamClosedEvent
    | _StartSpeechSynthesisStreamEventStream_ValidationException
    | _StartSpeechSynthesisStreamEventStream_ServiceQuotaExceededException
    | _StartSpeechSynthesisStreamEventStream_ServiceFailureException
    | _StartSpeechSynthesisStreamEventStream_ThrottlingException
)
StartSpeechSynthesisStreamEventStream: TypeAlias = AnyIterator[
    _StartSpeechSynthesisStreamEventStream
]


def serialize_event_json(value: _StartSpeechSynthesisStreamEventStream) -> bytes:
    match value:
        case {"AudioEvent": payload}:
            import aws_sdk_polly.types.audio_event

            return aws_sdk_polly.types.audio_event.serialize_event_json(payload)
        case {"StreamClosedEvent": payload}:
            import aws_sdk_polly.types.stream_closed_event

            return aws_sdk_polly.types.stream_closed_event.serialize_event_json(payload)
        case {"ValidationException": payload}:
            import aws_sdk_polly.errors.validation_exception

            return aws_sdk_polly.errors.validation_exception.serialize_event_json(
                payload
            )
        case {"ServiceQuotaExceededException": payload}:
            import aws_sdk_polly.errors.service_quota_exceeded_exception

            return aws_sdk_polly.errors.service_quota_exceeded_exception.serialize_event_json(
                payload
            )
        case {"ServiceFailureException": payload}:
            import aws_sdk_polly.errors.service_failure_exception

            return aws_sdk_polly.errors.service_failure_exception.serialize_event_json(
                payload
            )
        case {"ThrottlingException": payload}:
            import aws_sdk_polly.errors.throttling_exception

            return aws_sdk_polly.errors.throttling_exception.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"StartSpeechSynthesisStreamEventStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _StartSpeechSynthesisStreamEventStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "ValidationException":
                import aws_sdk_polly.errors.validation_exception

                raise aws_sdk_polly.errors.validation_exception.ValidationException(
                    aws_sdk_polly.errors.validation_exception.deserialize_event_json(
                        message
                    )
                )
            case "ServiceQuotaExceededException":
                import aws_sdk_polly.errors.service_quota_exceeded_exception

                raise aws_sdk_polly.errors.service_quota_exceeded_exception.ServiceQuotaExceededException(
                    aws_sdk_polly.errors.service_quota_exceeded_exception.deserialize_event_json(
                        message
                    )
                )
            case "ServiceFailureException":
                import aws_sdk_polly.errors.service_failure_exception

                raise aws_sdk_polly.errors.service_failure_exception.ServiceFailureException(
                    aws_sdk_polly.errors.service_failure_exception.deserialize_event_json(
                        message
                    )
                )
            case "ThrottlingException":
                import aws_sdk_polly.errors.throttling_exception

                raise aws_sdk_polly.errors.throttling_exception.ThrottlingException(
                    aws_sdk_polly.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(
            f"StartSpeechSynthesisStreamEventStream: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "AudioEvent":
            import aws_sdk_polly.types.audio_event

            return {
                "AudioEvent": aws_sdk_polly.types.audio_event.deserialize_event_json(
                    message
                )
            }
        case "StreamClosedEvent":
            import aws_sdk_polly.types.stream_closed_event

            return {
                "StreamClosedEvent": aws_sdk_polly.types.stream_closed_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"StartSpeechSynthesisStreamEventStream: unrecognized event-type {event_type!r}"
            )
