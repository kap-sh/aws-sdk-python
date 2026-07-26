"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointPerformance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_info
    import capo_sagemaker.types.inference_metrics


class EndpointPerformance(TypedDict, closed=True):
    metrics: NotRequired["capo_sagemaker.types.inference_metrics.InferenceMetrics"]
    """<p>The metrics for an existing endpoint.</p>"""
    endpoint_info: NotRequired["capo_sagemaker.types.endpoint_info.EndpointInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointPerformance) -> dict:
    out: dict = {}
    if "metrics" in value:
        import capo_sagemaker.types.inference_metrics

        out["Metrics"] = capo_sagemaker.types.inference_metrics.serialize_aws_json_1_1(
            value["metrics"]
        )
    if "endpoint_info" in value:
        import capo_sagemaker.types.endpoint_info

        out["EndpointInfo"] = capo_sagemaker.types.endpoint_info.serialize_aws_json_1_1(
            value["endpoint_info"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointPerformance:
    out: EndpointPerformance = {}  # type: ignore[typeddict-item]
    if "Metrics" in data:
        import capo_sagemaker.types.inference_metrics

        out["metrics"] = (
            capo_sagemaker.types.inference_metrics.deserialize_aws_json_1_1(
                data["Metrics"]
            )
        )
    if "EndpointInfo" in data:
        import capo_sagemaker.types.endpoint_info

        out["endpoint_info"] = (
            capo_sagemaker.types.endpoint_info.deserialize_aws_json_1_1(
                data["EndpointInfo"]
            )
        )
    return out
