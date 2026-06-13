"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseStreamResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.converse_stream_output


class ConverseStreamResponse(TypedDict):
    stream: NotRequired[
        "aws_sdk_bedrock_runtime.types.converse_stream_output.ConverseStreamOutput"
    ]
    """<p>The output stream that the model generated.</p>"""
