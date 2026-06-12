"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingPolicyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.predictive_scaling_max_capacity_breach_behavior
    import aws_sdk_application_auto_scaling.types.predictive_scaling_max_capacity_buffer
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_specifications
    import aws_sdk_application_auto_scaling.types.predictive_scaling_mode
    import aws_sdk_application_auto_scaling.types.predictive_scaling_scheduling_buffer_time


class PredictiveScalingPolicyConfiguration(TypedDict):
    metric_specifications: "aws_sdk_application_auto_scaling.types.predictive_scaling_metric_specifications.PredictiveScalingMetricSpecifications"
    """<p> This structure includes the metrics and target utilization to use for predictive scaling. </p> <p>This is an array, but we currently only support a single metric specification. That is, you can specify a target value and a single metric pair, or a target value and one scaling metric and one load metric.</p>"""
    mode: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_mode.PredictiveScalingMode"
    ]
    """<p> The predictive scaling mode. Defaults to <code>ForecastOnly</code> if not specified. </p>"""
    scheduling_buffer_time: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_scheduling_buffer_time.PredictiveScalingSchedulingBufferTime"
    ]
    """<p> The amount of time, in seconds, that the start time can be advanced. </p> <p>The value must be less than the forecast interval duration of 3600 seconds (60 minutes). Defaults to 300 seconds if not specified. </p>"""
    max_capacity_breach_behavior: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_max_capacity_breach_behavior.PredictiveScalingMaxCapacityBreachBehavior"
    ]
    """<p> Defines the behavior that should be applied if the forecast capacity approaches or exceeds the maximum capacity. Defaults to <code>HonorMaxCapacity</code> if not specified. </p>"""
    max_capacity_buffer: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_max_capacity_buffer.PredictiveScalingMaxCapacityBuffer"
    ]
    """<p> The size of the capacity buffer to use when the forecast capacity is close to or exceeds the maximum capacity. The value is specified as a percentage relative to the forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer, such that if the forecast capacity is 50, and the maximum capacity is 40, then the effective maximum capacity is 55. </p> <p>Required if the <code>MaxCapacityBreachBehavior</code> property is set to <code>IncreaseMaxCapacity</code>, and cannot be used otherwise.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingPolicyConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_specifications

    out["MetricSpecifications"] = (
        aws_sdk_application_auto_scaling.types.predictive_scaling_metric_specifications.serialize_aws_json_1_1(
            value["metric_specifications"]
        )
    )
    if "mode" in value:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_mode

        out["Mode"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_mode.serialize_aws_json_1_1(
                value["mode"]
            )
        )
    if "scheduling_buffer_time" in value:
        out["SchedulingBufferTime"] = value["scheduling_buffer_time"]
    if "max_capacity_breach_behavior" in value:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_max_capacity_breach_behavior

        out["MaxCapacityBreachBehavior"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_max_capacity_breach_behavior.serialize_aws_json_1_1(
                value["max_capacity_breach_behavior"]
            )
        )
    if "max_capacity_buffer" in value:
        out["MaxCapacityBuffer"] = value["max_capacity_buffer"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictiveScalingPolicyConfiguration:
    out: PredictiveScalingPolicyConfiguration = {}  # type: ignore[typeddict-item]
    if "MetricSpecifications" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_specifications

        out["metric_specifications"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_metric_specifications.deserialize_aws_json_1_1(
                data["MetricSpecifications"]
            )
        )
    else:
        raise DeserializationError(
            "PredictiveScalingPolicyConfiguration.metric_specifications required"
        )
    if "Mode" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_mode

        out["mode"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    if "SchedulingBufferTime" in data:
        out["scheduling_buffer_time"] = data["SchedulingBufferTime"]
    if "MaxCapacityBreachBehavior" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_max_capacity_breach_behavior

        out["max_capacity_breach_behavior"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_max_capacity_breach_behavior.deserialize_aws_json_1_1(
                data["MaxCapacityBreachBehavior"]
            )
        )
    if "MaxCapacityBuffer" in data:
        out["max_capacity_buffer"] = data["MaxCapacityBuffer"]
    return out
