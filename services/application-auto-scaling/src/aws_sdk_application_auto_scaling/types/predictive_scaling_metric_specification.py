"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingMetricSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.metric_scale
    import aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification
    import aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_load_metric_specification
    import aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_metric_pair_specification
    import aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_scaling_metric_specification


class PredictiveScalingMetricSpecification(TypedDict):
    target_value: "aws_sdk_application_auto_scaling.types.metric_scale.MetricScale"
    """<p> Specifies the target utilization. </p>"""
    predefined_metric_pair_specification: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_metric_pair_specification.PredictiveScalingPredefinedMetricPairSpecification"
    ]
    """<p> The predefined metric pair specification that determines the appropriate scaling metric and load metric to use. </p>"""
    predefined_scaling_metric_specification: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_scaling_metric_specification.PredictiveScalingPredefinedScalingMetricSpecification"
    ]
    """<p> The predefined scaling metric specification. </p>"""
    predefined_load_metric_specification: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_load_metric_specification.PredictiveScalingPredefinedLoadMetricSpecification"
    ]
    """<p> The predefined load metric specification. </p>"""
    customized_scaling_metric_specification: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification.PredictiveScalingCustomizedMetricSpecification"
    ]
    """<p> The customized scaling metric specification. </p>"""
    customized_load_metric_specification: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification.PredictiveScalingCustomizedMetricSpecification"
    ]
    """<p> The customized load metric specification. </p>"""
    customized_capacity_metric_specification: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification.PredictiveScalingCustomizedMetricSpecification"
    ]
    """<p> The customized capacity metric specification. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingMetricSpecification) -> dict:
    out: dict = {}
    out["TargetValue"] = value["target_value"]
    if "predefined_metric_pair_specification" in value:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_metric_pair_specification

        out["PredefinedMetricPairSpecification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_metric_pair_specification.serialize_aws_json_1_1(
                value["predefined_metric_pair_specification"]
            )
        )
    if "predefined_scaling_metric_specification" in value:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_scaling_metric_specification

        out["PredefinedScalingMetricSpecification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_scaling_metric_specification.serialize_aws_json_1_1(
                value["predefined_scaling_metric_specification"]
            )
        )
    if "predefined_load_metric_specification" in value:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_load_metric_specification

        out["PredefinedLoadMetricSpecification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_load_metric_specification.serialize_aws_json_1_1(
                value["predefined_load_metric_specification"]
            )
        )
    if "customized_scaling_metric_specification" in value:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification

        out["CustomizedScalingMetricSpecification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification.serialize_aws_json_1_1(
                value["customized_scaling_metric_specification"]
            )
        )
    if "customized_load_metric_specification" in value:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification

        out["CustomizedLoadMetricSpecification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification.serialize_aws_json_1_1(
                value["customized_load_metric_specification"]
            )
        )
    if "customized_capacity_metric_specification" in value:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification

        out["CustomizedCapacityMetricSpecification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification.serialize_aws_json_1_1(
                value["customized_capacity_metric_specification"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictiveScalingMetricSpecification:
    out: PredictiveScalingMetricSpecification = {}  # type: ignore[typeddict-item]
    if "TargetValue" in data:
        out["target_value"] = data["TargetValue"]
    else:
        raise DeserializationError(
            "PredictiveScalingMetricSpecification.target_value required"
        )
    if "PredefinedMetricPairSpecification" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_metric_pair_specification

        out["predefined_metric_pair_specification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_metric_pair_specification.deserialize_aws_json_1_1(
                data["PredefinedMetricPairSpecification"]
            )
        )
    if "PredefinedScalingMetricSpecification" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_scaling_metric_specification

        out["predefined_scaling_metric_specification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_scaling_metric_specification.deserialize_aws_json_1_1(
                data["PredefinedScalingMetricSpecification"]
            )
        )
    if "PredefinedLoadMetricSpecification" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_load_metric_specification

        out["predefined_load_metric_specification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_predefined_load_metric_specification.deserialize_aws_json_1_1(
                data["PredefinedLoadMetricSpecification"]
            )
        )
    if "CustomizedScalingMetricSpecification" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification

        out["customized_scaling_metric_specification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification.deserialize_aws_json_1_1(
                data["CustomizedScalingMetricSpecification"]
            )
        )
    if "CustomizedLoadMetricSpecification" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification

        out["customized_load_metric_specification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification.deserialize_aws_json_1_1(
                data["CustomizedLoadMetricSpecification"]
            )
        )
    if "CustomizedCapacityMetricSpecification" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification

        out["customized_capacity_metric_specification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_customized_metric_specification.deserialize_aws_json_1_1(
                data["CustomizedCapacityMetricSpecification"]
            )
        )
    return out
