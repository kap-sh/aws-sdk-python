"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStreamResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_output


class InvokeModelWithBidirectionalStreamResponse(TypedDict):
    body: "aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_output.InvokeModelWithBidirectionalStreamOutput"
    """<p>Streaming response from the model in the format specified by the <code>BidirectionalOutputPayloadPart</code> header.</p>"""
