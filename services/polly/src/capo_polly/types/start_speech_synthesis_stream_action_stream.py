"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisStreamActionStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_polly._iter import AnyIterator
from capo_polly._protocol.eventstream import Message

if TYPE_CHECKING:
    import capo_polly.types.close_stream_event
    import capo_polly.types.text_event


class _StartSpeechSynthesisStreamActionStream_TextEvent(TypedDict, closed=True):
    TextEvent: "capo_polly.types.text_event.TextEvent"


class _StartSpeechSynthesisStreamActionStream_CloseStreamEvent(TypedDict, closed=True):
    CloseStreamEvent: "capo_polly.types.close_stream_event.CloseStreamEvent"


_StartSpeechSynthesisStreamActionStream: TypeAlias = (
    _StartSpeechSynthesisStreamActionStream_TextEvent
    | _StartSpeechSynthesisStreamActionStream_CloseStreamEvent
)
StartSpeechSynthesisStreamActionStream: TypeAlias = AnyIterator[
    _StartSpeechSynthesisStreamActionStream
]


def serialize_event_json(value: _StartSpeechSynthesisStreamActionStream) -> bytes:
    match value:
        case {"TextEvent": payload}:
            import capo_polly.types.text_event

            return capo_polly.types.text_event.serialize_event_json(payload)
        case {"CloseStreamEvent": payload}:
            import capo_polly.types.close_stream_event

            return capo_polly.types.close_stream_event.serialize_event_json(payload)
        case _:
            raise ValueError(
                f"StartSpeechSynthesisStreamActionStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _StartSpeechSynthesisStreamActionStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    event_type = headers.get(":event-type")
    match event_type:
        case "TextEvent":
            import capo_polly.types.text_event

            return {
                "TextEvent": capo_polly.types.text_event.deserialize_event_json(message)
            }
        case "CloseStreamEvent":
            import capo_polly.types.close_stream_event

            return {
                "CloseStreamEvent": capo_polly.types.close_stream_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"StartSpeechSynthesisStreamActionStream: unrecognized event-type {event_type!r}"
            )
