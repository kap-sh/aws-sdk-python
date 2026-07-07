"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobInferenceBenchmark``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_output_configuration
    import aws_sdk_sagemaker.types.inference_metrics
    import aws_sdk_sagemaker.types.invocation_end_time
    import aws_sdk_sagemaker.types.invocation_start_time
    import aws_sdk_sagemaker.types.model_configuration
    import aws_sdk_sagemaker.types.recommendation_failure_reason
    import aws_sdk_sagemaker.types.recommendation_metrics


class RecommendationJobInferenceBenchmark(TypedDict, closed=True):
    metrics: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_metrics.RecommendationMetrics"
    ]
    endpoint_metrics: NotRequired[
        "aws_sdk_sagemaker.types.inference_metrics.InferenceMetrics"
    ]
    endpoint_configuration: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_output_configuration.EndpointOutputConfiguration"
    ]
    model_configuration: NotRequired[
        "aws_sdk_sagemaker.types.model_configuration.ModelConfiguration"
    ]
    failure_reason: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_failure_reason.RecommendationFailureReason"
    ]
    """<p>The reason why a benchmark failed.</p>"""
    invocation_end_time: NotRequired[
        "aws_sdk_sagemaker.types.invocation_end_time.InvocationEndTime"
    ]
    """<p>A timestamp that shows when the benchmark completed.</p>"""
    invocation_start_time: NotRequired[
        "aws_sdk_sagemaker.types.invocation_start_time.InvocationStartTime"
    ]
    """<p>A timestamp that shows when the benchmark started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobInferenceBenchmark) -> dict:
    out: dict = {}
    if "metrics" in value:
        import aws_sdk_sagemaker.types.recommendation_metrics

        out["Metrics"] = (
            aws_sdk_sagemaker.types.recommendation_metrics.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    if "endpoint_metrics" in value:
        import aws_sdk_sagemaker.types.inference_metrics

        out["EndpointMetrics"] = (
            aws_sdk_sagemaker.types.inference_metrics.serialize_aws_json_1_1(
                value["endpoint_metrics"]
            )
        )
    if "endpoint_configuration" in value:
        import aws_sdk_sagemaker.types.endpoint_output_configuration

        out["EndpointConfiguration"] = (
            aws_sdk_sagemaker.types.endpoint_output_configuration.serialize_aws_json_1_1(
                value["endpoint_configuration"]
            )
        )
    if "model_configuration" in value:
        import aws_sdk_sagemaker.types.model_configuration

        out["ModelConfiguration"] = (
            aws_sdk_sagemaker.types.model_configuration.serialize_aws_json_1_1(
                value["model_configuration"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "invocation_end_time" in value:
        import aws_sdk_sagemaker.types.invocation_end_time

        out["InvocationEndTime"] = (
            aws_sdk_sagemaker.types.invocation_end_time.serialize_aws_json_1_1(
                value["invocation_end_time"]
            )
        )
    if "invocation_start_time" in value:
        import aws_sdk_sagemaker.types.invocation_start_time

        out["InvocationStartTime"] = (
            aws_sdk_sagemaker.types.invocation_start_time.serialize_aws_json_1_1(
                value["invocation_start_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationJobInferenceBenchmark:
    out: RecommendationJobInferenceBenchmark = {}  # type: ignore[typeddict-item]
    if "Metrics" in data:
        import aws_sdk_sagemaker.types.recommendation_metrics

        out["metrics"] = (
            aws_sdk_sagemaker.types.recommendation_metrics.deserialize_aws_json_1_1(
                data["Metrics"]
            )
        )
    if "EndpointMetrics" in data:
        import aws_sdk_sagemaker.types.inference_metrics

        out["endpoint_metrics"] = (
            aws_sdk_sagemaker.types.inference_metrics.deserialize_aws_json_1_1(
                data["EndpointMetrics"]
            )
        )
    if "EndpointConfiguration" in data:
        import aws_sdk_sagemaker.types.endpoint_output_configuration

        out["endpoint_configuration"] = (
            aws_sdk_sagemaker.types.endpoint_output_configuration.deserialize_aws_json_1_1(
                data["EndpointConfiguration"]
            )
        )
    if "ModelConfiguration" in data:
        import aws_sdk_sagemaker.types.model_configuration

        out["model_configuration"] = (
            aws_sdk_sagemaker.types.model_configuration.deserialize_aws_json_1_1(
                data["ModelConfiguration"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "InvocationEndTime" in data:
        import aws_sdk_sagemaker.types.invocation_end_time

        out["invocation_end_time"] = (
            aws_sdk_sagemaker.types.invocation_end_time.deserialize_aws_json_1_1(
                data["InvocationEndTime"]
            )
        )
    if "InvocationStartTime" in data:
        import aws_sdk_sagemaker.types.invocation_start_time

        out["invocation_start_time"] = (
            aws_sdk_sagemaker.types.invocation_start_time.deserialize_aws_json_1_1(
                data["InvocationStartTime"]
            )
        )
    return out
