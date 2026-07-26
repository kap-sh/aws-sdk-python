"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StartConversationResponseEventStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_lex_runtime_v2._iter import AnyIterator
from capo_lex_runtime_v2._protocol.eventstream import Message

if TYPE_CHECKING:
    import capo_lex_runtime_v2.errors.access_denied_exception
    import capo_lex_runtime_v2.errors.bad_gateway_exception
    import capo_lex_runtime_v2.errors.conflict_exception
    import capo_lex_runtime_v2.errors.dependency_failed_exception
    import capo_lex_runtime_v2.errors.internal_server_exception
    import capo_lex_runtime_v2.errors.resource_not_found_exception
    import capo_lex_runtime_v2.errors.throttling_exception
    import capo_lex_runtime_v2.errors.validation_exception
    import capo_lex_runtime_v2.types.audio_response_event
    import capo_lex_runtime_v2.types.heartbeat_event
    import capo_lex_runtime_v2.types.intent_result_event
    import capo_lex_runtime_v2.types.playback_interruption_event
    import capo_lex_runtime_v2.types.text_response_event
    import capo_lex_runtime_v2.types.transcript_event


class _StartConversationResponseEventStream_PlaybackInterruptionEvent(
    TypedDict, closed=True
):
    PlaybackInterruptionEvent: "capo_lex_runtime_v2.types.playback_interruption_event.PlaybackInterruptionEvent"


class _StartConversationResponseEventStream_TranscriptEvent(TypedDict, closed=True):
    TranscriptEvent: "capo_lex_runtime_v2.types.transcript_event.TranscriptEvent"


class _StartConversationResponseEventStream_IntentResultEvent(TypedDict, closed=True):
    IntentResultEvent: "capo_lex_runtime_v2.types.intent_result_event.IntentResultEvent"


class _StartConversationResponseEventStream_TextResponseEvent(TypedDict, closed=True):
    TextResponseEvent: "capo_lex_runtime_v2.types.text_response_event.TextResponseEvent"


class _StartConversationResponseEventStream_AudioResponseEvent(TypedDict, closed=True):
    AudioResponseEvent: (
        "capo_lex_runtime_v2.types.audio_response_event.AudioResponseEvent"
    )


class _StartConversationResponseEventStream_HeartbeatEvent(TypedDict, closed=True):
    HeartbeatEvent: "capo_lex_runtime_v2.types.heartbeat_event.HeartbeatEvent"


class _StartConversationResponseEventStream_AccessDeniedException(
    TypedDict, closed=True
):
    AccessDeniedException: (
        "capo_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException_"
    )


class _StartConversationResponseEventStream_ResourceNotFoundException(
    TypedDict, closed=True
):
    ResourceNotFoundException: "capo_lex_runtime_v2.errors.resource_not_found_exception.ResourceNotFoundException_"


class _StartConversationResponseEventStream_ValidationException(TypedDict, closed=True):
    ValidationException: (
        "capo_lex_runtime_v2.errors.validation_exception.ValidationException_"
    )


class _StartConversationResponseEventStream_ThrottlingException(TypedDict, closed=True):
    ThrottlingException: (
        "capo_lex_runtime_v2.errors.throttling_exception.ThrottlingException_"
    )


class _StartConversationResponseEventStream_InternalServerException(
    TypedDict, closed=True
):
    InternalServerException: (
        "capo_lex_runtime_v2.errors.internal_server_exception.InternalServerException_"
    )


class _StartConversationResponseEventStream_ConflictException(TypedDict, closed=True):
    ConflictException: (
        "capo_lex_runtime_v2.errors.conflict_exception.ConflictException_"
    )


class _StartConversationResponseEventStream_DependencyFailedException(
    TypedDict, closed=True
):
    DependencyFailedException: "capo_lex_runtime_v2.errors.dependency_failed_exception.DependencyFailedException_"


class _StartConversationResponseEventStream_BadGatewayException(TypedDict, closed=True):
    BadGatewayException: (
        "capo_lex_runtime_v2.errors.bad_gateway_exception.BadGatewayException_"
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
            import capo_lex_runtime_v2.types.playback_interruption_event

            return capo_lex_runtime_v2.types.playback_interruption_event.serialize_event_json(
                payload
            )
        case {"TranscriptEvent": payload}:
            import capo_lex_runtime_v2.types.transcript_event

            return capo_lex_runtime_v2.types.transcript_event.serialize_event_json(
                payload
            )
        case {"IntentResultEvent": payload}:
            import capo_lex_runtime_v2.types.intent_result_event

            return capo_lex_runtime_v2.types.intent_result_event.serialize_event_json(
                payload
            )
        case {"TextResponseEvent": payload}:
            import capo_lex_runtime_v2.types.text_response_event

            return capo_lex_runtime_v2.types.text_response_event.serialize_event_json(
                payload
            )
        case {"AudioResponseEvent": payload}:
            import capo_lex_runtime_v2.types.audio_response_event

            return capo_lex_runtime_v2.types.audio_response_event.serialize_event_json(
                payload
            )
        case {"HeartbeatEvent": payload}:
            import capo_lex_runtime_v2.types.heartbeat_event

            return capo_lex_runtime_v2.types.heartbeat_event.serialize_event_json(
                payload
            )
        case {"AccessDeniedException": payload}:
            import capo_lex_runtime_v2.errors.access_denied_exception

            return (
                capo_lex_runtime_v2.errors.access_denied_exception.serialize_event_json(
                    payload
                )
            )
        case {"ResourceNotFoundException": payload}:
            import capo_lex_runtime_v2.errors.resource_not_found_exception

            return capo_lex_runtime_v2.errors.resource_not_found_exception.serialize_event_json(
                payload
            )
        case {"ValidationException": payload}:
            import capo_lex_runtime_v2.errors.validation_exception

            return capo_lex_runtime_v2.errors.validation_exception.serialize_event_json(
                payload
            )
        case {"ThrottlingException": payload}:
            import capo_lex_runtime_v2.errors.throttling_exception

            return capo_lex_runtime_v2.errors.throttling_exception.serialize_event_json(
                payload
            )
        case {"InternalServerException": payload}:
            import capo_lex_runtime_v2.errors.internal_server_exception

            return capo_lex_runtime_v2.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"ConflictException": payload}:
            import capo_lex_runtime_v2.errors.conflict_exception

            return capo_lex_runtime_v2.errors.conflict_exception.serialize_event_json(
                payload
            )
        case {"DependencyFailedException": payload}:
            import capo_lex_runtime_v2.errors.dependency_failed_exception

            return capo_lex_runtime_v2.errors.dependency_failed_exception.serialize_event_json(
                payload
            )
        case {"BadGatewayException": payload}:
            import capo_lex_runtime_v2.errors.bad_gateway_exception

            return (
                capo_lex_runtime_v2.errors.bad_gateway_exception.serialize_event_json(
                    payload
                )
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
                import capo_lex_runtime_v2.errors.access_denied_exception

                raise capo_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException(
                    capo_lex_runtime_v2.errors.access_denied_exception.deserialize_event_json(
                        message
                    )
                )
            case "ResourceNotFoundException":
                import capo_lex_runtime_v2.errors.resource_not_found_exception

                raise capo_lex_runtime_v2.errors.resource_not_found_exception.ResourceNotFoundException(
                    capo_lex_runtime_v2.errors.resource_not_found_exception.deserialize_event_json(
                        message
                    )
                )
            case "ValidationException":
                import capo_lex_runtime_v2.errors.validation_exception

                raise capo_lex_runtime_v2.errors.validation_exception.ValidationException(
                    capo_lex_runtime_v2.errors.validation_exception.deserialize_event_json(
                        message
                    )
                )
            case "ThrottlingException":
                import capo_lex_runtime_v2.errors.throttling_exception

                raise capo_lex_runtime_v2.errors.throttling_exception.ThrottlingException(
                    capo_lex_runtime_v2.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
            case "InternalServerException":
                import capo_lex_runtime_v2.errors.internal_server_exception

                raise capo_lex_runtime_v2.errors.internal_server_exception.InternalServerException(
                    capo_lex_runtime_v2.errors.internal_server_exception.deserialize_event_json(
                        message
                    )
                )
            case "ConflictException":
                import capo_lex_runtime_v2.errors.conflict_exception

                raise capo_lex_runtime_v2.errors.conflict_exception.ConflictException(
                    capo_lex_runtime_v2.errors.conflict_exception.deserialize_event_json(
                        message
                    )
                )
            case "DependencyFailedException":
                import capo_lex_runtime_v2.errors.dependency_failed_exception

                raise capo_lex_runtime_v2.errors.dependency_failed_exception.DependencyFailedException(
                    capo_lex_runtime_v2.errors.dependency_failed_exception.deserialize_event_json(
                        message
                    )
                )
            case "BadGatewayException":
                import capo_lex_runtime_v2.errors.bad_gateway_exception

                raise capo_lex_runtime_v2.errors.bad_gateway_exception.BadGatewayException(
                    capo_lex_runtime_v2.errors.bad_gateway_exception.deserialize_event_json(
                        message
                    )
                )
        raise ValueError(
            f"StartConversationResponseEventStream: unrecognized error-type {error_type!r}"
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "PlaybackInterruptionEvent":
            import capo_lex_runtime_v2.types.playback_interruption_event

            return {
                "PlaybackInterruptionEvent": capo_lex_runtime_v2.types.playback_interruption_event.deserialize_event_json(
                    message
                )
            }
        case "TranscriptEvent":
            import capo_lex_runtime_v2.types.transcript_event

            return {
                "TranscriptEvent": capo_lex_runtime_v2.types.transcript_event.deserialize_event_json(
                    message
                )
            }
        case "IntentResultEvent":
            import capo_lex_runtime_v2.types.intent_result_event

            return {
                "IntentResultEvent": capo_lex_runtime_v2.types.intent_result_event.deserialize_event_json(
                    message
                )
            }
        case "TextResponseEvent":
            import capo_lex_runtime_v2.types.text_response_event

            return {
                "TextResponseEvent": capo_lex_runtime_v2.types.text_response_event.deserialize_event_json(
                    message
                )
            }
        case "AudioResponseEvent":
            import capo_lex_runtime_v2.types.audio_response_event

            return {
                "AudioResponseEvent": capo_lex_runtime_v2.types.audio_response_event.deserialize_event_json(
                    message
                )
            }
        case "HeartbeatEvent":
            import capo_lex_runtime_v2.types.heartbeat_event

            return {
                "HeartbeatEvent": capo_lex_runtime_v2.types.heartbeat_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"StartConversationResponseEventStream: unrecognized event-type {event_type!r}"
            )
