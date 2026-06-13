"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithResponseStreamResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.mime_type
    import aws_sdk_bedrock_runtime.types.performance_config_latency
    import aws_sdk_bedrock_runtime.types.response_stream
    import aws_sdk_bedrock_runtime.types.service_tier_type


class InvokeModelWithResponseStreamResponse(TypedDict):
    body: "aws_sdk_bedrock_runtime.types.response_stream.ResponseStream"
    """<p>Inference response from the model in the format specified by the <code>contentType</code> header. To see the format and content of this field for different models, refer to <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html\">Inference parameters</a>.</p>"""
    content_type: "aws_sdk_bedrock_runtime.types.mime_type.MimeType"
    """<p>The MIME type of the inference result.</p>"""
    performance_config_latency: NotRequired[
        "aws_sdk_bedrock_runtime.types.performance_config_latency.PerformanceConfigLatency"
    ]
    """<p>Model performance settings for the request.</p>"""
    service_tier: NotRequired[
        "aws_sdk_bedrock_runtime.types.service_tier_type.ServiceTierType"
    ]
    """<p>Specifies the processing tier type used for serving the request.</p>"""
