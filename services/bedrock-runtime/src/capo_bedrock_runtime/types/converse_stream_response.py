"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.converse_stream_output


class ConverseStreamResponse(TypedDict, closed=True):
    stream: NotRequired[
        "capo_bedrock_runtime.types.converse_stream_output.ConverseStreamOutput"
    ]
    """<p>The output stream that the model generated.</p>"""
