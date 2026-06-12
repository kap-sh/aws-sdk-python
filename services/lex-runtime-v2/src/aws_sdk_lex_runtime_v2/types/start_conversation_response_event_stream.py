"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StartConversationResponseEventStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_lex_runtime_v2.errors import DeserializationError, SerializationError

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
        "aws_sdk_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException"
    )


class _StartConversationResponseEventStream_ResourceNotFoundException(TypedDict):
    ResourceNotFoundException: "aws_sdk_lex_runtime_v2.errors.resource_not_found_exception.ResourceNotFoundException"


class _StartConversationResponseEventStream_ValidationException(TypedDict):
    ValidationException: (
        "aws_sdk_lex_runtime_v2.errors.validation_exception.ValidationException"
    )


class _StartConversationResponseEventStream_ThrottlingException(TypedDict):
    ThrottlingException: (
        "aws_sdk_lex_runtime_v2.errors.throttling_exception.ThrottlingException"
    )


class _StartConversationResponseEventStream_InternalServerException(TypedDict):
    InternalServerException: "aws_sdk_lex_runtime_v2.errors.internal_server_exception.InternalServerException"


class _StartConversationResponseEventStream_ConflictException(TypedDict):
    ConflictException: (
        "aws_sdk_lex_runtime_v2.errors.conflict_exception.ConflictException"
    )


class _StartConversationResponseEventStream_DependencyFailedException(TypedDict):
    DependencyFailedException: "aws_sdk_lex_runtime_v2.errors.dependency_failed_exception.DependencyFailedException"


class _StartConversationResponseEventStream_BadGatewayException(TypedDict):
    BadGatewayException: (
        "aws_sdk_lex_runtime_v2.errors.bad_gateway_exception.BadGatewayException"
    )


StartConversationResponseEventStream: TypeAlias = (
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


# --- restJson1 ser/de ---
def serialize_json(value: StartConversationResponseEventStream) -> dict:
    if "PlaybackInterruptionEvent" in value:
        import aws_sdk_lex_runtime_v2.types.playback_interruption_event

        return {
            "PlaybackInterruptionEvent": aws_sdk_lex_runtime_v2.types.playback_interruption_event.serialize_json(
                value["PlaybackInterruptionEvent"]
            )
        }
    elif "TranscriptEvent" in value:
        import aws_sdk_lex_runtime_v2.types.transcript_event

        return {
            "TranscriptEvent": aws_sdk_lex_runtime_v2.types.transcript_event.serialize_json(
                value["TranscriptEvent"]
            )
        }
    elif "IntentResultEvent" in value:
        import aws_sdk_lex_runtime_v2.types.intent_result_event

        return {
            "IntentResultEvent": aws_sdk_lex_runtime_v2.types.intent_result_event.serialize_json(
                value["IntentResultEvent"]
            )
        }
    elif "TextResponseEvent" in value:
        import aws_sdk_lex_runtime_v2.types.text_response_event

        return {
            "TextResponseEvent": aws_sdk_lex_runtime_v2.types.text_response_event.serialize_json(
                value["TextResponseEvent"]
            )
        }
    elif "AudioResponseEvent" in value:
        import aws_sdk_lex_runtime_v2.types.audio_response_event

        return {
            "AudioResponseEvent": aws_sdk_lex_runtime_v2.types.audio_response_event.serialize_json(
                value["AudioResponseEvent"]
            )
        }
    elif "HeartbeatEvent" in value:
        import aws_sdk_lex_runtime_v2.types.heartbeat_event

        return {
            "HeartbeatEvent": aws_sdk_lex_runtime_v2.types.heartbeat_event.serialize_json(
                value["HeartbeatEvent"]
            )
        }
    elif "AccessDeniedException" in value:
        import aws_sdk_lex_runtime_v2.errors.access_denied_exception

        return {
            "AccessDeniedException": aws_sdk_lex_runtime_v2.errors.access_denied_exception.serialize_json(
                value["AccessDeniedException"]
            )
        }
    elif "ResourceNotFoundException" in value:
        import aws_sdk_lex_runtime_v2.errors.resource_not_found_exception

        return {
            "ResourceNotFoundException": aws_sdk_lex_runtime_v2.errors.resource_not_found_exception.serialize_json(
                value["ResourceNotFoundException"]
            )
        }
    elif "ValidationException" in value:
        import aws_sdk_lex_runtime_v2.errors.validation_exception

        return {
            "ValidationException": aws_sdk_lex_runtime_v2.errors.validation_exception.serialize_json(
                value["ValidationException"]
            )
        }
    elif "ThrottlingException" in value:
        import aws_sdk_lex_runtime_v2.errors.throttling_exception

        return {
            "ThrottlingException": aws_sdk_lex_runtime_v2.errors.throttling_exception.serialize_json(
                value["ThrottlingException"]
            )
        }
    elif "InternalServerException" in value:
        import aws_sdk_lex_runtime_v2.errors.internal_server_exception

        return {
            "InternalServerException": aws_sdk_lex_runtime_v2.errors.internal_server_exception.serialize_json(
                value["InternalServerException"]
            )
        }
    elif "ConflictException" in value:
        import aws_sdk_lex_runtime_v2.errors.conflict_exception

        return {
            "ConflictException": aws_sdk_lex_runtime_v2.errors.conflict_exception.serialize_json(
                value["ConflictException"]
            )
        }
    elif "DependencyFailedException" in value:
        import aws_sdk_lex_runtime_v2.errors.dependency_failed_exception

        return {
            "DependencyFailedException": aws_sdk_lex_runtime_v2.errors.dependency_failed_exception.serialize_json(
                value["DependencyFailedException"]
            )
        }
    elif "BadGatewayException" in value:
        import aws_sdk_lex_runtime_v2.errors.bad_gateway_exception

        return {
            "BadGatewayException": aws_sdk_lex_runtime_v2.errors.bad_gateway_exception.serialize_json(
                value["BadGatewayException"]
            )
        }
    else:
        raise SerializationError(
            "StartConversationResponseEventStream: no variant present"
        )


def deserialize_json(data: dict) -> StartConversationResponseEventStream:
    if "PlaybackInterruptionEvent" in data:
        import aws_sdk_lex_runtime_v2.types.playback_interruption_event

        return {
            "PlaybackInterruptionEvent": aws_sdk_lex_runtime_v2.types.playback_interruption_event.deserialize_json(
                data["PlaybackInterruptionEvent"]
            )
        }
    elif "TranscriptEvent" in data:
        import aws_sdk_lex_runtime_v2.types.transcript_event

        return {
            "TranscriptEvent": aws_sdk_lex_runtime_v2.types.transcript_event.deserialize_json(
                data["TranscriptEvent"]
            )
        }
    elif "IntentResultEvent" in data:
        import aws_sdk_lex_runtime_v2.types.intent_result_event

        return {
            "IntentResultEvent": aws_sdk_lex_runtime_v2.types.intent_result_event.deserialize_json(
                data["IntentResultEvent"]
            )
        }
    elif "TextResponseEvent" in data:
        import aws_sdk_lex_runtime_v2.types.text_response_event

        return {
            "TextResponseEvent": aws_sdk_lex_runtime_v2.types.text_response_event.deserialize_json(
                data["TextResponseEvent"]
            )
        }
    elif "AudioResponseEvent" in data:
        import aws_sdk_lex_runtime_v2.types.audio_response_event

        return {
            "AudioResponseEvent": aws_sdk_lex_runtime_v2.types.audio_response_event.deserialize_json(
                data["AudioResponseEvent"]
            )
        }
    elif "HeartbeatEvent" in data:
        import aws_sdk_lex_runtime_v2.types.heartbeat_event

        return {
            "HeartbeatEvent": aws_sdk_lex_runtime_v2.types.heartbeat_event.deserialize_json(
                data["HeartbeatEvent"]
            )
        }
    elif "AccessDeniedException" in data:
        import aws_sdk_lex_runtime_v2.errors.access_denied_exception

        return {
            "AccessDeniedException": aws_sdk_lex_runtime_v2.errors.access_denied_exception.deserialize_json(
                data["AccessDeniedException"]
            )
        }
    elif "ResourceNotFoundException" in data:
        import aws_sdk_lex_runtime_v2.errors.resource_not_found_exception

        return {
            "ResourceNotFoundException": aws_sdk_lex_runtime_v2.errors.resource_not_found_exception.deserialize_json(
                data["ResourceNotFoundException"]
            )
        }
    elif "ValidationException" in data:
        import aws_sdk_lex_runtime_v2.errors.validation_exception

        return {
            "ValidationException": aws_sdk_lex_runtime_v2.errors.validation_exception.deserialize_json(
                data["ValidationException"]
            )
        }
    elif "ThrottlingException" in data:
        import aws_sdk_lex_runtime_v2.errors.throttling_exception

        return {
            "ThrottlingException": aws_sdk_lex_runtime_v2.errors.throttling_exception.deserialize_json(
                data["ThrottlingException"]
            )
        }
    elif "InternalServerException" in data:
        import aws_sdk_lex_runtime_v2.errors.internal_server_exception

        return {
            "InternalServerException": aws_sdk_lex_runtime_v2.errors.internal_server_exception.deserialize_json(
                data["InternalServerException"]
            )
        }
    elif "ConflictException" in data:
        import aws_sdk_lex_runtime_v2.errors.conflict_exception

        return {
            "ConflictException": aws_sdk_lex_runtime_v2.errors.conflict_exception.deserialize_json(
                data["ConflictException"]
            )
        }
    elif "DependencyFailedException" in data:
        import aws_sdk_lex_runtime_v2.errors.dependency_failed_exception

        return {
            "DependencyFailedException": aws_sdk_lex_runtime_v2.errors.dependency_failed_exception.deserialize_json(
                data["DependencyFailedException"]
            )
        }
    elif "BadGatewayException" in data:
        import aws_sdk_lex_runtime_v2.errors.bad_gateway_exception

        return {
            "BadGatewayException": aws_sdk_lex_runtime_v2.errors.bad_gateway_exception.deserialize_json(
                data["BadGatewayException"]
            )
        }
    else:
        raise DeserializationError(
            "StartConversationResponseEventStream: no recognized variant key"
        )
