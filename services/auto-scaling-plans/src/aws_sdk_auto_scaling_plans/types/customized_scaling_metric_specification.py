"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#CustomizedScalingMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling_plans.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.metric_dimensions
    import aws_sdk_auto_scaling_plans.types.metric_name
    import aws_sdk_auto_scaling_plans.types.metric_namespace
    import aws_sdk_auto_scaling_plans.types.metric_statistic
    import aws_sdk_auto_scaling_plans.types.metric_unit


class CustomizedScalingMetricSpecification(TypedDict, closed=True):
    metric_name: "aws_sdk_auto_scaling_plans.types.metric_name.MetricName"
    """<p>The name of the metric.</p>"""
    namespace: "aws_sdk_auto_scaling_plans.types.metric_namespace.MetricNamespace"
    """<p>The namespace of the metric.</p>"""
    dimensions: NotRequired[
        "aws_sdk_auto_scaling_plans.types.metric_dimensions.MetricDimensions"
    ]
    """<p>The dimensions of the metric.</p> <p>Conditional: If you published your metric with dimensions, you must specify the same dimensions in your customized scaling metric specification.</p>"""
    statistic: "aws_sdk_auto_scaling_plans.types.metric_statistic.MetricStatistic"
    """<p>The statistic of the metric.</p>"""
    unit: NotRequired["aws_sdk_auto_scaling_plans.types.metric_unit.MetricUnit"]
    """<p>The unit of the metric. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomizedScalingMetricSpecification) -> dict:
    out: dict = {}
    out["MetricName"] = value["metric_name"]
    out["Namespace"] = value["namespace"]
    if "dimensions" in value:
        import aws_sdk_auto_scaling_plans.types.metric_dimensions

        out["Dimensions"] = (
            aws_sdk_auto_scaling_plans.types.metric_dimensions.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    import aws_sdk_auto_scaling_plans.types.metric_statistic

    out["Statistic"] = (
        aws_sdk_auto_scaling_plans.types.metric_statistic.serialize_aws_json_1_1(
            value["statistic"]
        )
    )
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomizedScalingMetricSpecification:
    out: CustomizedScalingMetricSpecification = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    else:
        raise DeserializationError(
            "CustomizedScalingMetricSpecification.metric_name required"
        )
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    else:
        raise DeserializationError(
            "CustomizedScalingMetricSpecification.namespace required"
        )
    if "Dimensions" in data:
        import aws_sdk_auto_scaling_plans.types.metric_dimensions

        out["dimensions"] = (
            aws_sdk_auto_scaling_plans.types.metric_dimensions.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    if "Statistic" in data:
        import aws_sdk_auto_scaling_plans.types.metric_statistic

        out["statistic"] = (
            aws_sdk_auto_scaling_plans.types.metric_statistic.deserialize_aws_json_1_1(
                data["Statistic"]
            )
        )
    else:
        raise DeserializationError(
            "CustomizedScalingMetricSpecification.statistic required"
        )
    if "Unit" in data:
        out["unit"] = data["Unit"]
    return out
