"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InvokeEndpointAsyncInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime.types.custom_attributes_header
    import aws_sdk_sagemaker_runtime.types.endpoint_name
    import aws_sdk_sagemaker_runtime.types.filename_header
    import aws_sdk_sagemaker_runtime.types.header
    import aws_sdk_sagemaker_runtime.types.inference_id
    import aws_sdk_sagemaker_runtime.types.input_location_header
    import aws_sdk_sagemaker_runtime.types.invocation_timeout_seconds_header
    import aws_sdk_sagemaker_runtime.types.request_ttl_seconds_header
    import aws_sdk_sagemaker_runtime.types.s3_output_path_extension_header


class InvokeEndpointAsyncInput(TypedDict):
    endpoint_name: "aws_sdk_sagemaker_runtime.types.endpoint_name.EndpointName"
    r"""<p>The name of the endpoint that you specified when you created the endpoint using the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html\">CreateEndpoint</a> API.</p>"""
    content_type: NotRequired["aws_sdk_sagemaker_runtime.types.header.Header"]
    """<p>The MIME type of the input data in the request body.</p>"""
    accept: NotRequired["aws_sdk_sagemaker_runtime.types.header.Header"]
    """<p>The desired MIME type of the inference response from the model container.</p>"""
    custom_attributes: NotRequired[
        "aws_sdk_sagemaker_runtime.types.custom_attributes_header.CustomAttributesHeader"
    ]
    r"""<p>Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker AI endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in <a href=\"https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6\">Section 3.3.6. Field Value Components</a> of the Hypertext Transfer Protocol (HTTP/1.1). </p> <p>The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with <code>Trace ID:</code> in your post-processing function. </p> <p>This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker AI Python SDK. </p>"""
    inference_id: NotRequired[
        "aws_sdk_sagemaker_runtime.types.inference_id.InferenceId"
    ]
    """<p>The identifier for the inference request. Amazon SageMaker AI will generate an identifier for you if none is specified. </p>"""
    input_location: NotRequired[
        "aws_sdk_sagemaker_runtime.types.input_location_header.InputLocationHeader"
    ]
    """<p>The Amazon S3 URI where the inference request payload is stored.</p>"""
    s3_output_path_extension: NotRequired[
        "aws_sdk_sagemaker_runtime.types.s3_output_path_extension_header.S3OutputPathExtensionHeader"
    ]
    """<p>The path extension that is appended to the Amazon S3 output path where the inference response payload is stored.</p>"""
    filename: NotRequired[
        "aws_sdk_sagemaker_runtime.types.filename_header.FilenameHeader"
    ]
    """<p>The filename for the inference response payload stored in Amazon S3. If not specified, Amazon SageMaker AI generates a filename based on the inference ID.</p>"""
    request_ttl_seconds: NotRequired[
        "aws_sdk_sagemaker_runtime.types.request_ttl_seconds_header.RequestTTLSecondsHeader"
    ]
    """<p>Maximum age in seconds a request can be in the queue before it is marked as expired. The default is 6 hours, or 21,600 seconds.</p>"""
    invocation_timeout_seconds: NotRequired[
        "aws_sdk_sagemaker_runtime.types.invocation_timeout_seconds_header.InvocationTimeoutSecondsHeader"
    ]
    """<p>Maximum amount of time in seconds a request can be processed before it is marked as expired. The default is 15 minutes, or 900 seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeEndpointAsyncInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InvokeEndpointAsyncInput:
    out: InvokeEndpointAsyncInput = {}  # type: ignore[typeddict-item]
    return out
