"""Generated from Smithy shape ``com.amazonaws.sagemaker#PredefinedMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.string


class PredefinedMetricSpecification(TypedDict, closed=True):
    predefined_metric_type: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The metric type. You can only apply SageMaker metric types to SageMaker endpoints.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredefinedMetricSpecification) -> dict:
    out: dict = {}
    if "predefined_metric_type" in value:
        out["PredefinedMetricType"] = value["predefined_metric_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredefinedMetricSpecification:
    out: PredefinedMetricSpecification = {}  # type: ignore[typeddict-item]
    if "PredefinedMetricType" in data:
        out["predefined_metric_type"] = data["PredefinedMetricType"]
    return out
