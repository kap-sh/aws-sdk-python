"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisStreamOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_polly.types.start_speech_synthesis_stream_event_stream


class StartSpeechSynthesisStreamOutput(TypedDict):
    event_stream: NotRequired[
        "aws_sdk_polly.types.start_speech_synthesis_stream_event_stream.StartSpeechSynthesisStreamEventStream"
    ]
    """<p>The output event stream that contains synthesized audio events and stream status events.</p>"""
