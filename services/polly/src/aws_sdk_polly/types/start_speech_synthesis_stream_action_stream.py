"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisStreamActionStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_polly.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_polly.types.close_stream_event
    import aws_sdk_polly.types.text_event


class _StartSpeechSynthesisStreamActionStream_TextEvent(TypedDict):
    TextEvent: "aws_sdk_polly.types.text_event.TextEvent"


class _StartSpeechSynthesisStreamActionStream_CloseStreamEvent(TypedDict):
    CloseStreamEvent: "aws_sdk_polly.types.close_stream_event.CloseStreamEvent"


StartSpeechSynthesisStreamActionStream: TypeAlias = (
    _StartSpeechSynthesisStreamActionStream_TextEvent
    | _StartSpeechSynthesisStreamActionStream_CloseStreamEvent
)


# --- restJson1 ser/de ---
def serialize_json(value: StartSpeechSynthesisStreamActionStream) -> dict:
    if "TextEvent" in value:
        import aws_sdk_polly.types.text_event

        return {
            "TextEvent": aws_sdk_polly.types.text_event.serialize_json(
                value["TextEvent"]
            )
        }
    elif "CloseStreamEvent" in value:
        import aws_sdk_polly.types.close_stream_event

        return {
            "CloseStreamEvent": aws_sdk_polly.types.close_stream_event.serialize_json(
                value["CloseStreamEvent"]
            )
        }
    else:
        raise SerializationError(
            "StartSpeechSynthesisStreamActionStream: no variant present"
        )


def deserialize_json(data: dict) -> StartSpeechSynthesisStreamActionStream:
    if "TextEvent" in data:
        import aws_sdk_polly.types.text_event

        return {
            "TextEvent": aws_sdk_polly.types.text_event.deserialize_json(
                data["TextEvent"]
            )
        }
    elif "CloseStreamEvent" in data:
        import aws_sdk_polly.types.close_stream_event

        return {
            "CloseStreamEvent": aws_sdk_polly.types.close_stream_event.deserialize_json(
                data["CloseStreamEvent"]
            )
        }
    else:
        raise DeserializationError(
            "StartSpeechSynthesisStreamActionStream: no recognized variant key"
        )
