"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobInferenceBenchmark``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_output_configuration
    import capo_sagemaker.types.inference_metrics
    import capo_sagemaker.types.invocation_end_time
    import capo_sagemaker.types.invocation_start_time
    import capo_sagemaker.types.model_configuration
    import capo_sagemaker.types.recommendation_failure_reason
    import capo_sagemaker.types.recommendation_metrics


class RecommendationJobInferenceBenchmark(TypedDict, closed=True):
    metrics: NotRequired[
        "capo_sagemaker.types.recommendation_metrics.RecommendationMetrics"
    ]
    endpoint_metrics: NotRequired[
        "capo_sagemaker.types.inference_metrics.InferenceMetrics"
    ]
    endpoint_configuration: NotRequired[
        "capo_sagemaker.types.endpoint_output_configuration.EndpointOutputConfiguration"
    ]
    model_configuration: NotRequired[
        "capo_sagemaker.types.model_configuration.ModelConfiguration"
    ]
    failure_reason: NotRequired[
        "capo_sagemaker.types.recommendation_failure_reason.RecommendationFailureReason"
    ]
    """<p>The reason why a benchmark failed.</p>"""
    invocation_end_time: NotRequired[
        "capo_sagemaker.types.invocation_end_time.InvocationEndTime"
    ]
    """<p>A timestamp that shows when the benchmark completed.</p>"""
    invocation_start_time: NotRequired[
        "capo_sagemaker.types.invocation_start_time.InvocationStartTime"
    ]
    """<p>A timestamp that shows when the benchmark started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobInferenceBenchmark) -> dict:
    out: dict = {}
    if "metrics" in value:
        import capo_sagemaker.types.recommendation_metrics

        out["Metrics"] = (
            capo_sagemaker.types.recommendation_metrics.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    if "endpoint_metrics" in value:
        import capo_sagemaker.types.inference_metrics

        out["EndpointMetrics"] = (
            capo_sagemaker.types.inference_metrics.serialize_aws_json_1_1(
                value["endpoint_metrics"]
            )
        )
    if "endpoint_configuration" in value:
        import capo_sagemaker.types.endpoint_output_configuration

        out["EndpointConfiguration"] = (
            capo_sagemaker.types.endpoint_output_configuration.serialize_aws_json_1_1(
                value["endpoint_configuration"]
            )
        )
    if "model_configuration" in value:
        import capo_sagemaker.types.model_configuration

        out["ModelConfiguration"] = (
            capo_sagemaker.types.model_configuration.serialize_aws_json_1_1(
                value["model_configuration"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "invocation_end_time" in value:
        import capo_sagemaker.types.invocation_end_time

        out["InvocationEndTime"] = (
            capo_sagemaker.types.invocation_end_time.serialize_aws_json_1_1(
                value["invocation_end_time"]
            )
        )
    if "invocation_start_time" in value:
        import capo_sagemaker.types.invocation_start_time

        out["InvocationStartTime"] = (
            capo_sagemaker.types.invocation_start_time.serialize_aws_json_1_1(
                value["invocation_start_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationJobInferenceBenchmark:
    out: RecommendationJobInferenceBenchmark = {}  # type: ignore[typeddict-item]
    if "Metrics" in data:
        import capo_sagemaker.types.recommendation_metrics

        out["metrics"] = (
            capo_sagemaker.types.recommendation_metrics.deserialize_aws_json_1_1(
                data["Metrics"]
            )
        )
    if "EndpointMetrics" in data:
        import capo_sagemaker.types.inference_metrics

        out["endpoint_metrics"] = (
            capo_sagemaker.types.inference_metrics.deserialize_aws_json_1_1(
                data["EndpointMetrics"]
            )
        )
    if "EndpointConfiguration" in data:
        import capo_sagemaker.types.endpoint_output_configuration

        out["endpoint_configuration"] = (
            capo_sagemaker.types.endpoint_output_configuration.deserialize_aws_json_1_1(
                data["EndpointConfiguration"]
            )
        )
    if "ModelConfiguration" in data:
        import capo_sagemaker.types.model_configuration

        out["model_configuration"] = (
            capo_sagemaker.types.model_configuration.deserialize_aws_json_1_1(
                data["ModelConfiguration"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "InvocationEndTime" in data:
        import capo_sagemaker.types.invocation_end_time

        out["invocation_end_time"] = (
            capo_sagemaker.types.invocation_end_time.deserialize_aws_json_1_1(
                data["InvocationEndTime"]
            )
        )
    if "InvocationStartTime" in data:
        import capo_sagemaker.types.invocation_start_time

        out["invocation_start_time"] = (
            capo_sagemaker.types.invocation_start_time.deserialize_aws_json_1_1(
                data["InvocationStartTime"]
            )
        )
    return out
