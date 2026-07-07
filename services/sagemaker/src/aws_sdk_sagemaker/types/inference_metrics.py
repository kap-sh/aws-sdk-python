"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.integer


class InferenceMetrics(TypedDict, closed=True):
    max_invocations: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The expected maximum number of requests per minute for the instance.</p>"""
    model_latency: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The expected model latency at maximum invocations per minute for the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceMetrics) -> dict:
    out: dict = {}
    if "max_invocations" in value:
        out["MaxInvocations"] = value["max_invocations"]
    if "model_latency" in value:
        out["ModelLatency"] = value["model_latency"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceMetrics:
    out: InferenceMetrics = {}  # type: ignore[typeddict-item]
    if "MaxInvocations" in data:
        out["max_invocations"] = data["MaxInvocations"]
    if "ModelLatency" in data:
        out["model_latency"] = data["ModelLatency"]
    return out
