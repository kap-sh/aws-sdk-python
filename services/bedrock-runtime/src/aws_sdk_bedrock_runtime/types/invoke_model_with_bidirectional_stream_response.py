"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_output


class InvokeModelWithBidirectionalStreamResponse(TypedDict, closed=True):
    body: "aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_output.InvokeModelWithBidirectionalStreamOutput"
    """<p>Streaming response from the model in the format specified by the <code>BidirectionalOutputPayloadPart</code> header.</p>"""
