"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InvokeEndpointAsyncOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime.types.header


class InvokeEndpointAsyncOutput(TypedDict):
    inference_id: NotRequired["aws_sdk_sagemaker_runtime.types.header.Header"]
    """<p>Identifier for an inference request. This will be the same as the <code>InferenceId</code> specified in the input. Amazon SageMaker AI will generate an identifier for you if you do not specify one.</p>"""
    output_location: NotRequired["aws_sdk_sagemaker_runtime.types.header.Header"]
    """<p>The Amazon S3 URI where the inference response payload is stored.</p>"""
    failure_location: NotRequired["aws_sdk_sagemaker_runtime.types.header.Header"]
    """<p>The Amazon S3 URI where the inference failure response payload is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeEndpointAsyncOutput) -> dict:
    out: dict = {}
    if "inference_id" in value:
        out["InferenceId"] = value["inference_id"]
    return out


def deserialize_json(data: dict) -> InvokeEndpointAsyncOutput:
    out: InvokeEndpointAsyncOutput = {}  # type: ignore[typeddict-item]
    if "InferenceId" in data:
        out["inference_id"] = data["InferenceId"]
    return out
