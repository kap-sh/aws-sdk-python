"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StartConversationRequestEventStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_lex_runtime_v2._iter import AnyIterator
from aws_sdk_lex_runtime_v2._protocol.eventstream import Message

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.audio_input_event
    import aws_sdk_lex_runtime_v2.types.configuration_event
    import aws_sdk_lex_runtime_v2.types.disconnection_event
    import aws_sdk_lex_runtime_v2.types.dtmf_input_event
    import aws_sdk_lex_runtime_v2.types.playback_completion_event
    import aws_sdk_lex_runtime_v2.types.text_input_event


class _StartConversationRequestEventStream_ConfigurationEvent(TypedDict):
    ConfigurationEvent: (
        "aws_sdk_lex_runtime_v2.types.configuration_event.ConfigurationEvent"
    )


class _StartConversationRequestEventStream_AudioInputEvent(TypedDict):
    AudioInputEvent: "aws_sdk_lex_runtime_v2.types.audio_input_event.AudioInputEvent"


class _StartConversationRequestEventStream_DTMFInputEvent(TypedDict):
    DTMFInputEvent: "aws_sdk_lex_runtime_v2.types.dtmf_input_event.DTMFInputEvent"


class _StartConversationRequestEventStream_TextInputEvent(TypedDict):
    TextInputEvent: "aws_sdk_lex_runtime_v2.types.text_input_event.TextInputEvent"


class _StartConversationRequestEventStream_PlaybackCompletionEvent(TypedDict):
    PlaybackCompletionEvent: (
        "aws_sdk_lex_runtime_v2.types.playback_completion_event.PlaybackCompletionEvent"
    )


class _StartConversationRequestEventStream_DisconnectionEvent(TypedDict):
    DisconnectionEvent: (
        "aws_sdk_lex_runtime_v2.types.disconnection_event.DisconnectionEvent"
    )


_StartConversationRequestEventStream: TypeAlias = (
    _StartConversationRequestEventStream_ConfigurationEvent
    | _StartConversationRequestEventStream_AudioInputEvent
    | _StartConversationRequestEventStream_DTMFInputEvent
    | _StartConversationRequestEventStream_TextInputEvent
    | _StartConversationRequestEventStream_PlaybackCompletionEvent
    | _StartConversationRequestEventStream_DisconnectionEvent
)
StartConversationRequestEventStream: TypeAlias = AnyIterator[
    _StartConversationRequestEventStream
]


def serialize_event_json(value: _StartConversationRequestEventStream) -> bytes:
    match value:
        case {"ConfigurationEvent": payload}:
            import aws_sdk_lex_runtime_v2.types.configuration_event

            return (
                aws_sdk_lex_runtime_v2.types.configuration_event.serialize_event_json(
                    payload
                )
            )
        case {"AudioInputEvent": payload}:
            import aws_sdk_lex_runtime_v2.types.audio_input_event

            return aws_sdk_lex_runtime_v2.types.audio_input_event.serialize_event_json(
                payload
            )
        case {"DTMFInputEvent": payload}:
            import aws_sdk_lex_runtime_v2.types.dtmf_input_event

            return aws_sdk_lex_runtime_v2.types.dtmf_input_event.serialize_event_json(
                payload
            )
        case {"TextInputEvent": payload}:
            import aws_sdk_lex_runtime_v2.types.text_input_event

            return aws_sdk_lex_runtime_v2.types.text_input_event.serialize_event_json(
                payload
            )
        case {"PlaybackCompletionEvent": payload}:
            import aws_sdk_lex_runtime_v2.types.playback_completion_event

            return aws_sdk_lex_runtime_v2.types.playback_completion_event.serialize_event_json(
                payload
            )
        case {"DisconnectionEvent": payload}:
            import aws_sdk_lex_runtime_v2.types.disconnection_event

            return (
                aws_sdk_lex_runtime_v2.types.disconnection_event.serialize_event_json(
                    payload
                )
            )
        case _:
            raise ValueError(
                f"StartConversationRequestEventStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _StartConversationRequestEventStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    event_type = headers.get(":event-type")
    match event_type:
        case "ConfigurationEvent":
            import aws_sdk_lex_runtime_v2.types.configuration_event

            return {
                "ConfigurationEvent": aws_sdk_lex_runtime_v2.types.configuration_event.deserialize_event_json(
                    message
                )
            }
        case "AudioInputEvent":
            import aws_sdk_lex_runtime_v2.types.audio_input_event

            return {
                "AudioInputEvent": aws_sdk_lex_runtime_v2.types.audio_input_event.deserialize_event_json(
                    message
                )
            }
        case "DTMFInputEvent":
            import aws_sdk_lex_runtime_v2.types.dtmf_input_event

            return {
                "DTMFInputEvent": aws_sdk_lex_runtime_v2.types.dtmf_input_event.deserialize_event_json(
                    message
                )
            }
        case "TextInputEvent":
            import aws_sdk_lex_runtime_v2.types.text_input_event

            return {
                "TextInputEvent": aws_sdk_lex_runtime_v2.types.text_input_event.deserialize_event_json(
                    message
                )
            }
        case "PlaybackCompletionEvent":
            import aws_sdk_lex_runtime_v2.types.playback_completion_event

            return {
                "PlaybackCompletionEvent": aws_sdk_lex_runtime_v2.types.playback_completion_event.deserialize_event_json(
                    message
                )
            }
        case "DisconnectionEvent":
            import aws_sdk_lex_runtime_v2.types.disconnection_event

            return {
                "DisconnectionEvent": aws_sdk_lex_runtime_v2.types.disconnection_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"StartConversationRequestEventStream: unrecognized event-type {event_type!r}"
            )
