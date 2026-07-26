"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisStreamEventStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_polly._iter import AnyIterator
from capo_polly._protocol.eventstream import Message

if TYPE_CHECKING:
    import capo_polly.errors.service_failure_exception
    import capo_polly.errors.service_quota_exceeded_exception
    import capo_polly.errors.throttling_exception
    import capo_polly.errors.validation_exception
    import capo_polly.types.audio_event
    import capo_polly.types.stream_closed_event


class _StartSpeechSynthesisStreamEventStream_AudioEvent(TypedDict, closed=True):
    AudioEvent: "capo_polly.types.audio_event.AudioEvent"


class _StartSpeechSynthesisStreamEventStream_StreamClosedEvent(TypedDict, closed=True):
    StreamClosedEvent: "capo_polly.types.stream_closed_event.StreamClosedEvent"


class _StartSpeechSynthesisStreamEventStream_ValidationException(
    TypedDict, closed=True
):
    ValidationException: "capo_polly.errors.validation_exception.ValidationException_"


class _StartSpeechSynthesisStreamEventStream_ServiceQuotaExceededException(
    TypedDict, closed=True
):
    ServiceQuotaExceededException: "capo_polly.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _StartSpeechSynthesisStreamEventStream_ServiceFailureException(
    TypedDict, closed=True
):
    ServiceFailureException: (
        "capo_polly.errors.service_failure_exception.ServiceFailureException_"
    )


class _StartSpeechSynthesisStreamEventStream_ThrottlingException(
    TypedDict, closed=True
):
    ThrottlingException: "capo_polly.errors.throttling_exception.ThrottlingException_"


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
            import capo_polly.types.audio_event

            return capo_polly.types.audio_event.serialize_event_json(payload)
        case {"StreamClosedEvent": payload}:
            import capo_polly.types.stream_closed_event

            return capo_polly.types.stream_closed_event.serialize_event_json(payload)
        case {"ValidationException": payload}:
            import capo_polly.errors.validation_exception

            return capo_polly.errors.validation_exception.serialize_event_json(payload)
        case {"ServiceQuotaExceededException": payload}:
            import capo_polly.errors.service_quota_exceeded_exception

            return (
                capo_polly.errors.service_quota_exceeded_exception.serialize_event_json(
                    payload
                )
            )
        case {"ServiceFailureException": payload}:
            import capo_polly.errors.service_failure_exception

            return capo_polly.errors.service_failure_exception.serialize_event_json(
                payload
            )
        case {"ThrottlingException": payload}:
            import capo_polly.errors.throttling_exception

            return capo_polly.errors.throttling_exception.serialize_event_json(payload)
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
                import capo_polly.errors.validation_exception

                raise capo_polly.errors.validation_exception.ValidationException(
                    capo_polly.errors.validation_exception.deserialize_event_json(
                        message
                    )
                )
            case "ServiceQuotaExceededException":
                import capo_polly.errors.service_quota_exceeded_exception

                raise capo_polly.errors.service_quota_exceeded_exception.ServiceQuotaExceededException(
                    capo_polly.errors.service_quota_exceeded_exception.deserialize_event_json(
                        message
                    )
                )
            case "ServiceFailureException":
                import capo_polly.errors.service_failure_exception

                raise capo_polly.errors.service_failure_exception.ServiceFailureException(
                    capo_polly.errors.service_failure_exception.deserialize_event_json(
                        message
                    )
                )
            case "ThrottlingException":
                import capo_polly.errors.throttling_exception

                raise capo_polly.errors.throttling_exception.ThrottlingException(
                    capo_polly.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(
            f"StartSpeechSynthesisStreamEventStream: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "AudioEvent":
            import capo_polly.types.audio_event

            return {
                "AudioEvent": capo_polly.types.audio_event.deserialize_event_json(
                    message
                )
            }
        case "StreamClosedEvent":
            import capo_polly.types.stream_closed_event

            return {
                "StreamClosedEvent": capo_polly.types.stream_closed_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"StartSpeechSynthesisStreamEventStream: unrecognized event-type {event_type!r}"
            )
