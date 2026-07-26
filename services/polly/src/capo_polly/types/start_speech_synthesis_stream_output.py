"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_polly.types.start_speech_synthesis_stream_event_stream


class StartSpeechSynthesisStreamOutput(TypedDict, closed=True):
    event_stream: NotRequired[
        "capo_polly.types.start_speech_synthesis_stream_event_stream.StartSpeechSynthesisStreamEventStream"
    ]
    """<p>The output event stream that contains synthesized audio events and stream status events.</p>"""
