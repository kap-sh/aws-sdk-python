"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobStoppingConditions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.flat_invocations
    import capo_sagemaker.types.integer
    import capo_sagemaker.types.model_latency_thresholds


class RecommendationJobStoppingConditions(TypedDict, closed=True):
    max_invocations: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The maximum number of requests per minute expected for the endpoint.</p>"""
    model_latency_thresholds: NotRequired[
        "capo_sagemaker.types.model_latency_thresholds.ModelLatencyThresholds"
    ]
    """<p>The interval of time taken by a model to respond as viewed from SageMaker. The interval includes the local communication time taken to send the request and to fetch the response from the container of a model and the time taken to complete the inference in the container.</p>"""
    flat_invocations: NotRequired[
        "capo_sagemaker.types.flat_invocations.FlatInvocations"
    ]
    """<p>Stops a load test when the number of invocations (TPS) peaks and flattens, which means that the instance has reached capacity. The default value is <code>Stop</code>. If you want the load test to continue after invocations have flattened, set the value to <code>Continue</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobStoppingConditions) -> dict:
    out: dict = {}
    if "max_invocations" in value:
        out["MaxInvocations"] = value["max_invocations"]
    if "model_latency_thresholds" in value:
        import capo_sagemaker.types.model_latency_thresholds

        out["ModelLatencyThresholds"] = (
            capo_sagemaker.types.model_latency_thresholds.serialize_aws_json_1_1(
                value["model_latency_thresholds"]
            )
        )
    if "flat_invocations" in value:
        import capo_sagemaker.types.flat_invocations

        out["FlatInvocations"] = (
            capo_sagemaker.types.flat_invocations.serialize_aws_json_1_1(
                value["flat_invocations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationJobStoppingConditions:
    out: RecommendationJobStoppingConditions = {}  # type: ignore[typeddict-item]
    if "MaxInvocations" in data:
        out["max_invocations"] = data["MaxInvocations"]
    if "ModelLatencyThresholds" in data:
        import capo_sagemaker.types.model_latency_thresholds

        out["model_latency_thresholds"] = (
            capo_sagemaker.types.model_latency_thresholds.deserialize_aws_json_1_1(
                data["ModelLatencyThresholds"]
            )
        )
    if "FlatInvocations" in data:
        import capo_sagemaker.types.flat_invocations

        out["flat_invocations"] = (
            capo_sagemaker.types.flat_invocations.deserialize_aws_json_1_1(
                data["FlatInvocations"]
            )
        )
    return out
