"""Generated from Smithy shape ``com.amazonaws.sagemaker#ScalingPolicyMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.integer


class ScalingPolicyMetric(TypedDict, closed=True):
    invocations_per_instance: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The number of invocations sent to a model, normalized by <code>InstanceCount</code> in each ProductionVariant. <code>1/numberOfInstances</code> is sent as the value on each request, where <code>numberOfInstances</code> is the number of active instances for the ProductionVariant behind the endpoint at the time of the request.</p>"""
    model_latency: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The interval of time taken by a model to respond as viewed from SageMaker. This interval includes the local communication times taken to send the request and to fetch the response from the container of a model and the time taken to complete the inference in the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPolicyMetric) -> dict:
    out: dict = {}
    if "invocations_per_instance" in value:
        out["InvocationsPerInstance"] = value["invocations_per_instance"]
    if "model_latency" in value:
        out["ModelLatency"] = value["model_latency"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingPolicyMetric:
    out: ScalingPolicyMetric = {}  # type: ignore[typeddict-item]
    if "InvocationsPerInstance" in data:
        out["invocations_per_instance"] = data["InvocationsPerInstance"]
    if "ModelLatency" in data:
        out["model_latency"] = data["ModelLatency"]
    return out
