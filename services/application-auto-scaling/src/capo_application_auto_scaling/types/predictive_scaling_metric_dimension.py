"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingMetricDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.predictive_scaling_metric_dimension_name
    import capo_application_auto_scaling.types.predictive_scaling_metric_dimension_value


class PredictiveScalingMetricDimension(TypedDict, closed=True):
    name: "capo_application_auto_scaling.types.predictive_scaling_metric_dimension_name.PredictiveScalingMetricDimensionName"
    """<p> The name of the dimension. </p>"""
    value: "capo_application_auto_scaling.types.predictive_scaling_metric_dimension_value.PredictiveScalingMetricDimensionValue"
    """<p> The value of the dimension. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingMetricDimension) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictiveScalingMetricDimension:
    out: PredictiveScalingMetricDimension = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PredictiveScalingMetricDimension.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("PredictiveScalingMetricDimension.value required")
    return out
