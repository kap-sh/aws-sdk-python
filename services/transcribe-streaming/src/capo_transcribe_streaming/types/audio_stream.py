"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#AudioStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transcribe_streaming._iter import AnyIterator
from capo_transcribe_streaming._protocol.eventstream import Message

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.audio_event
    import capo_transcribe_streaming.types.configuration_event


class _AudioStream_AudioEvent(TypedDict, closed=True):
    AudioEvent: "capo_transcribe_streaming.types.audio_event.AudioEvent"


class _AudioStream_ConfigurationEvent(TypedDict, closed=True):
    ConfigurationEvent: (
        "capo_transcribe_streaming.types.configuration_event.ConfigurationEvent"
    )


_AudioStream: TypeAlias = _AudioStream_AudioEvent | _AudioStream_ConfigurationEvent
AudioStream: TypeAlias = AnyIterator[_AudioStream]


def serialize_event_json(value: _AudioStream) -> bytes:
    match value:
        case {"AudioEvent": payload}:
            import capo_transcribe_streaming.types.audio_event

            return capo_transcribe_streaming.types.audio_event.serialize_event_json(
                payload
            )
        case {"ConfigurationEvent": payload}:
            import capo_transcribe_streaming.types.configuration_event

            return capo_transcribe_streaming.types.configuration_event.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"AudioStream: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _AudioStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")  # noqa: F841
    event_type = headers.get(":event-type")
    match event_type:
        case "AudioEvent":
            import capo_transcribe_streaming.types.audio_event

            return {
                "AudioEvent": capo_transcribe_streaming.types.audio_event.deserialize_event_json(
                    message
                )
            }
        case "ConfigurationEvent":
            import capo_transcribe_streaming.types.configuration_event

            return {
                "ConfigurationEvent": capo_transcribe_streaming.types.configuration_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(f"AudioStream: unrecognized event-type {event_type!r}")
