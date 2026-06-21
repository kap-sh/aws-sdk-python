"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StartConversationResponseEventStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_lex_runtime_v2._iter import AnyIterator
from aws_sdk_lex_runtime_v2._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.errors.access_denied_exception
    import aws_sdk_lex_runtime_v2.errors.bad_gateway_exception
    import aws_sdk_lex_runtime_v2.errors.conflict_exception
    import aws_sdk_lex_runtime_v2.errors.dependency_failed_exception
    import aws_sdk_lex_runtime_v2.errors.internal_server_exception
    import aws_sdk_lex_runtime_v2.errors.resource_not_found_exception
    import aws_sdk_lex_runtime_v2.errors.throttling_exception
    import aws_sdk_lex_runtime_v2.errors.validation_exception
    import aws_sdk_lex_runtime_v2.types.audio_response_event
    import aws_sdk_lex_runtime_v2.types.heartbeat_event
    import aws_sdk_lex_runtime_v2.types.intent_result_event
    import aws_sdk_lex_runtime_v2.types.playback_interruption_event
    import aws_sdk_lex_runtime_v2.types.text_response_event
    import aws_sdk_lex_runtime_v2.types.transcript_event


class _StartConversationResponseEventStream_PlaybackInterruptionEvent(TypedDict):
    PlaybackInterruptionEvent: "aws_sdk_lex_runtime_v2.types.playback_interruption_event.PlaybackInterruptionEvent"


class _StartConversationResponseEventStream_TranscriptEvent(TypedDict):
    TranscriptEvent: "aws_sdk_lex_runtime_v2.types.transcript_event.TranscriptEvent"


class _StartConversationResponseEventStream_IntentResultEvent(TypedDict):
    IntentResultEvent: (
        "aws_sdk_lex_runtime_v2.types.intent_result_event.IntentResultEvent"
    )


class _StartConversationResponseEventStream_TextResponseEvent(TypedDict):
    TextResponseEvent: (
        "aws_sdk_lex_runtime_v2.types.text_response_event.TextResponseEvent"
    )


class _StartConversationResponseEventStream_AudioResponseEvent(TypedDict):
    AudioResponseEvent: (
        "aws_sdk_lex_runtime_v2.types.audio_response_event.AudioResponseEvent"
    )


class _StartConversationResponseEventStream_HeartbeatEvent(TypedDict):
    HeartbeatEvent: "aws_sdk_lex_runtime_v2.types.heartbeat_event.HeartbeatEvent"


class _StartConversationResponseEventStream_AccessDeniedException(TypedDict):
    AccessDeniedException: (
        "aws_sdk_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException_"
    )


class _StartConversationResponseEventStream_ResourceNotFoundException(TypedDict):
    ResourceNotFoundException: "aws_sdk_lex_runtime_v2.errors.resource_not_found_exception.ResourceNotFoundException_"


class _StartConversationResponseEventStream_ValidationException(TypedDict):
    ValidationException: (
        "aws_sdk_lex_runtime_v2.errors.validation_exception.ValidationException_"
    )


class _StartConversationResponseEventStream_ThrottlingException(TypedDict):
    ThrottlingException: (
        "aws_sdk_lex_runtime_v2.errors.throttling_exception.ThrottlingException_"
    )


class _StartConversationResponseEventStream_InternalServerException(TypedDict):
    InternalServerException: "aws_sdk_lex_runtime_v2.errors.internal_server_exception.InternalServerException_"


class _StartConversationResponseEventStream_ConflictException(TypedDict):
    ConflictException: (
        "aws_sdk_lex_runtime_v2.errors.conflict_exception.ConflictException_"
    )


class _StartConversationResponseEventStream_DependencyFailedException(TypedDict):
    DependencyFailedException: "aws_sdk_lex_runtime_v2.errors.dependency_failed_exception.DependencyFailedException_"


class _StartConversationResponseEventStream_BadGatewayException(TypedDict):
    BadGatewayException: (
        "aws_sdk_lex_runtime_v2.errors.bad_gateway_exception.BadGatewayException_"
    )


_StartConversationResponseEventStream: TypeAlias = (
    _StartConversationResponseEventStream_PlaybackInterruptionEvent
    | _StartConversationResponseEventStream_TranscriptEvent
    | _StartConversationResponseEventStream_IntentResultEvent
    | _StartConversationResponseEventStream_TextResponseEvent
    | _StartConversationResponseEventStream_AudioResponseEvent
    | _StartConversationResponseEventStream_HeartbeatEvent
    | _StartConversationResponseEventStream_AccessDeniedException
    | _StartConversationResponseEventStream_ResourceNotFoundException
    | _StartConversationResponseEventStream_ValidationException
    | _StartConversationResponseEventStream_ThrottlingException
    | _StartConversationResponseEventStream_InternalServerException
    | _StartConversationResponseEventStream_ConflictException
    | _StartConversationResponseEventStream_DependencyFailedException
    | _StartConversationResponseEventStream_BadGatewayException
)
StartConversationResponseEventStream: TypeAlias = AnyIterator[
    _StartConversationResponseEventStream
]


def serialize_event_json(value: _StartConversationResponseEventStream) -> bytes:
    match value:
        case {"PlaybackInterruptionEvent": payload}:
            import aws_sdk_lex_runtime_v2.types.playback_interruption_event

            return aws_sdk_lex_runtime_v2.types.playback_interruption_event.serialize_event_json(
                payload
            )
        case {"TranscriptEvent": payload}:
            import aws_sdk_lex_runtime_v2.types.transcript_event

            return aws_sdk_lex_runtime_v2.types.transcript_event.serialize_event_json(
                payload
            )
        case {"IntentResultEvent": payload}:
            import aws_sdk_lex_runtime_v2.types.intent_result_event

            return (
                aws_sdk_lex_runtime_v2.types.intent_result_event.serialize_event_json(
                    payload
                )
            )
        case {"TextResponseEvent": payload}:
            import aws_sdk_lex_runtime_v2.types.text_response_event

            return (
                aws_sdk_lex_runtime_v2.types.text_response_event.serialize_event_json(
                    payload
                )
            )
        case {"AudioResponseEvent": payload}:
            import aws_sdk_lex_runtime_v2.types.audio_response_event

            return (
                aws_sdk_lex_runtime_v2.types.audio_response_event.serialize_event_json(
                    payload
                )
            )
        case {"HeartbeatEvent": payload}:
            import aws_sdk_lex_runtime_v2.types.heartbeat_event

            return aws_sdk_lex_runtime_v2.types.heartbeat_event.serialize_event_json(
                payload
            )
        case {"AccessDeniedException": payload}:
            import aws_sdk_lex_runtime_v2.errors.access_denied_exception

            return aws_sdk_lex_runtime_v2.errors.access_denied_exception.serialize_event_json(
                payload
            )
        case {"ResourceNotFoundException": payload}:
            import aws_sdk_lex_runtime_v2.errors.resource_not_found_exception

            return aws_sdk_lex_runtime_v2.errors.resource_not_found_exception.serialize_event_json(
                payload
            )
        case {"ValidationException": payload}:
            import aws_sdk_lex_runtime_v2.errors.validation_exception

            return (
                aws_sdk_lex_runtime_v2.errors.validation_exception.serialize_event_json(
                    payload
                )
            )
        case {"ThrottlingException": payload}:
            import aws_sdk_lex_runtime_v2.errors.throttling_exception

            return (
                aws_sdk_lex_runtime_v2.errors.throttling_exception.serialize_event_json(
                    payload
                )
            )
        case {"InternalServerException": payload}:
            import aws_sdk_lex_runtime_v2.errors.internal_server_exception

            return aws_sdk_lex_runtime_v2.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"ConflictException": payload}:
            import aws_sdk_lex_runtime_v2.errors.conflict_exception

            return (
                aws_sdk_lex_runtime_v2.errors.conflict_exception.serialize_event_json(
                    payload
                )
            )
        case {"DependencyFailedException": payload}:
            import aws_sdk_lex_runtime_v2.errors.dependency_failed_exception

            return aws_sdk_lex_runtime_v2.errors.dependency_failed_exception.serialize_event_json(
                payload
            )
        case {"BadGatewayException": payload}:
            import aws_sdk_lex_runtime_v2.errors.bad_gateway_exception

            return aws_sdk_lex_runtime_v2.errors.bad_gateway_exception.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"StartConversationResponseEventStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _StartConversationResponseEventStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    if message_type == "error":
        error_type = headers.get(":error-type")
        match error_type:
            case "AccessDeniedException":
                import aws_sdk_lex_runtime_v2.errors.access_denied_exception

                raise aws_sdk_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException(
                    aws_sdk_lex_runtime_v2.errors.access_denied_exception.deserialize_event_json(
                        message
                    )
                )
            case "ResourceNotFoundException":
                import aws_sdk_lex_runtime_v2.errors.resource_not_found_exception

                raise aws_sdk_lex_runtime_v2.errors.resource_not_found_exception.ResourceNotFoundException(
                    aws_sdk_lex_runtime_v2.errors.resource_not_found_exception.deserialize_event_json(
                        message
                    )
                )
            case "ValidationException":
                import aws_sdk_lex_runtime_v2.errors.validation_exception

                raise aws_sdk_lex_runtime_v2.errors.validation_exception.ValidationException(
                    aws_sdk_lex_runtime_v2.errors.validation_exception.deserialize_event_json(
                        message
                    )
                )
            case "ThrottlingException":
                import aws_sdk_lex_runtime_v2.errors.throttling_exception

                raise aws_sdk_lex_runtime_v2.errors.throttling_exception.ThrottlingException(
                    aws_sdk_lex_runtime_v2.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
            case "InternalServerException":
                import aws_sdk_lex_runtime_v2.errors.internal_server_exception

                raise aws_sdk_lex_runtime_v2.errors.internal_server_exception.InternalServerException(
                    aws_sdk_lex_runtime_v2.errors.internal_server_exception.deserialize_event_json(
                        message
                    )
                )
            case "ConflictException":
                import aws_sdk_lex_runtime_v2.errors.conflict_exception

                raise aws_sdk_lex_runtime_v2.errors.conflict_exception.ConflictException(
                    aws_sdk_lex_runtime_v2.errors.conflict_exception.deserialize_event_json(
                        message
                    )
                )
            case "DependencyFailedException":
                import aws_sdk_lex_runtime_v2.errors.dependency_failed_exception

                raise aws_sdk_lex_runtime_v2.errors.dependency_failed_exception.DependencyFailedException(
                    aws_sdk_lex_runtime_v2.errors.dependency_failed_exception.deserialize_event_json(
                        message
                    )
                )
            case "BadGatewayException":
                import aws_sdk_lex_runtime_v2.errors.bad_gateway_exception

                raise aws_sdk_lex_runtime_v2.errors.bad_gateway_exception.BadGatewayException(
                    aws_sdk_lex_runtime_v2.errors.bad_gateway_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(
            f"StartConversationResponseEventStream: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "PlaybackInterruptionEvent":
            import aws_sdk_lex_runtime_v2.types.playback_interruption_event

            return {
                "PlaybackInterruptionEvent": aws_sdk_lex_runtime_v2.types.playback_interruption_event.deserialize_event_json(
                    message
                )
            }
        case "TranscriptEvent":
            import aws_sdk_lex_runtime_v2.types.transcript_event

            return {
                "TranscriptEvent": aws_sdk_lex_runtime_v2.types.transcript_event.deserialize_event_json(
                    message
                )
            }
        case "IntentResultEvent":
            import aws_sdk_lex_runtime_v2.types.intent_result_event

            return {
                "IntentResultEvent": aws_sdk_lex_runtime_v2.types.intent_result_event.deserialize_event_json(
                    message
                )
            }
        case "TextResponseEvent":
            import aws_sdk_lex_runtime_v2.types.text_response_event

            return {
                "TextResponseEvent": aws_sdk_lex_runtime_v2.types.text_response_event.deserialize_event_json(
                    message
                )
            }
        case "AudioResponseEvent":
            import aws_sdk_lex_runtime_v2.types.audio_response_event

            return {
                "AudioResponseEvent": aws_sdk_lex_runtime_v2.types.audio_response_event.deserialize_event_json(
                    message
                )
            }
        case "HeartbeatEvent":
            import aws_sdk_lex_runtime_v2.types.heartbeat_event

            return {
                "HeartbeatEvent": aws_sdk_lex_runtime_v2.types.heartbeat_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"StartConversationResponseEventStream: unrecognized event-type {event_type!r}"
            )
