"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StartConversationRequestEventStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_lex_runtime_v2.errors import DeserializationError, SerializationError

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


StartConversationRequestEventStream: TypeAlias = (
    _StartConversationRequestEventStream_ConfigurationEvent
    | _StartConversationRequestEventStream_AudioInputEvent
    | _StartConversationRequestEventStream_DTMFInputEvent
    | _StartConversationRequestEventStream_TextInputEvent
    | _StartConversationRequestEventStream_PlaybackCompletionEvent
    | _StartConversationRequestEventStream_DisconnectionEvent
)


# --- restJson1 ser/de ---
def serialize_json(value: StartConversationRequestEventStream) -> dict:
    if "ConfigurationEvent" in value:
        import aws_sdk_lex_runtime_v2.types.configuration_event

        return {
            "ConfigurationEvent": aws_sdk_lex_runtime_v2.types.configuration_event.serialize_json(
                value["ConfigurationEvent"]
            )
        }
    elif "AudioInputEvent" in value:
        import aws_sdk_lex_runtime_v2.types.audio_input_event

        return {
            "AudioInputEvent": aws_sdk_lex_runtime_v2.types.audio_input_event.serialize_json(
                value["AudioInputEvent"]
            )
        }
    elif "DTMFInputEvent" in value:
        import aws_sdk_lex_runtime_v2.types.dtmf_input_event

        return {
            "DTMFInputEvent": aws_sdk_lex_runtime_v2.types.dtmf_input_event.serialize_json(
                value["DTMFInputEvent"]
            )
        }
    elif "TextInputEvent" in value:
        import aws_sdk_lex_runtime_v2.types.text_input_event

        return {
            "TextInputEvent": aws_sdk_lex_runtime_v2.types.text_input_event.serialize_json(
                value["TextInputEvent"]
            )
        }
    elif "PlaybackCompletionEvent" in value:
        import aws_sdk_lex_runtime_v2.types.playback_completion_event

        return {
            "PlaybackCompletionEvent": aws_sdk_lex_runtime_v2.types.playback_completion_event.serialize_json(
                value["PlaybackCompletionEvent"]
            )
        }
    elif "DisconnectionEvent" in value:
        import aws_sdk_lex_runtime_v2.types.disconnection_event

        return {
            "DisconnectionEvent": aws_sdk_lex_runtime_v2.types.disconnection_event.serialize_json(
                value["DisconnectionEvent"]
            )
        }
    else:
        raise SerializationError(
            "StartConversationRequestEventStream: no variant present"
        )


def deserialize_json(data: dict) -> StartConversationRequestEventStream:
    if "ConfigurationEvent" in data:
        import aws_sdk_lex_runtime_v2.types.configuration_event

        return {
            "ConfigurationEvent": aws_sdk_lex_runtime_v2.types.configuration_event.deserialize_json(
                data["ConfigurationEvent"]
            )
        }
    elif "AudioInputEvent" in data:
        import aws_sdk_lex_runtime_v2.types.audio_input_event

        return {
            "AudioInputEvent": aws_sdk_lex_runtime_v2.types.audio_input_event.deserialize_json(
                data["AudioInputEvent"]
            )
        }
    elif "DTMFInputEvent" in data:
        import aws_sdk_lex_runtime_v2.types.dtmf_input_event

        return {
            "DTMFInputEvent": aws_sdk_lex_runtime_v2.types.dtmf_input_event.deserialize_json(
                data["DTMFInputEvent"]
            )
        }
    elif "TextInputEvent" in data:
        import aws_sdk_lex_runtime_v2.types.text_input_event

        return {
            "TextInputEvent": aws_sdk_lex_runtime_v2.types.text_input_event.deserialize_json(
                data["TextInputEvent"]
            )
        }
    elif "PlaybackCompletionEvent" in data:
        import aws_sdk_lex_runtime_v2.types.playback_completion_event

        return {
            "PlaybackCompletionEvent": aws_sdk_lex_runtime_v2.types.playback_completion_event.deserialize_json(
                data["PlaybackCompletionEvent"]
            )
        }
    elif "DisconnectionEvent" in data:
        import aws_sdk_lex_runtime_v2.types.disconnection_event

        return {
            "DisconnectionEvent": aws_sdk_lex_runtime_v2.types.disconnection_event.deserialize_json(
                data["DisconnectionEvent"]
            )
        }
    else:
        raise DeserializationError(
            "StartConversationRequestEventStream: no recognized variant key"
        )
