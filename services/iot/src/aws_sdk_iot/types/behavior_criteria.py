"""Generated from Smithy shape ``com.amazonaws.iot#BehaviorCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.comparison_operator
    import aws_sdk_iot.types.consecutive_datapoints_to_alarm
    import aws_sdk_iot.types.consecutive_datapoints_to_clear
    import aws_sdk_iot.types.duration_seconds
    import aws_sdk_iot.types.machine_learning_detection_config
    import aws_sdk_iot.types.metric_value
    import aws_sdk_iot.types.statistical_threshold


class BehaviorCriteria(TypedDict):
    comparison_operator: NotRequired[
        "aws_sdk_iot.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The operator that relates the thing measured (<code>metric</code>) to the criteria (containing a <code>value</code> or <code>statisticalThreshold</code>). Valid operators include:</p> <ul> <li> <p> <code>string-list</code>: <code>in-set</code> and <code>not-in-set</code> </p> </li> <li> <p> <code>number-list</code>: <code>in-set</code> and <code>not-in-set</code> </p> </li> <li> <p> <code>ip-address-list</code>: <code>in-cidr-set</code> and <code>not-in-cidr-set</code> </p> </li> <li> <p> <code>number</code>: <code>less-than</code>, <code>less-than-equals</code>, <code>greater-than</code>, and <code>greater-than-equals</code> </p> </li> </ul>"""
    value: NotRequired["aws_sdk_iot.types.metric_value.MetricValue"]
    """<p>The value to be compared with the <code>metric</code>.</p>"""
    duration_seconds: NotRequired["aws_sdk_iot.types.duration_seconds.DurationSeconds"]
    """<p>Use this to specify the time duration over which the behavior is evaluated, for those criteria that have a time dimension (for example, <code>NUM_MESSAGES_SENT</code>). For a <code>statisticalThreshhold</code> metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank. Cannot be used with list-based metric datatypes.</p>"""
    consecutive_datapoints_to_alarm: NotRequired[
        "aws_sdk_iot.types.consecutive_datapoints_to_alarm.ConsecutiveDatapointsToAlarm"
    ]
    """<p>If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.</p>"""
    consecutive_datapoints_to_clear: NotRequired[
        "aws_sdk_iot.types.consecutive_datapoints_to_clear.ConsecutiveDatapointsToClear"
    ]
    """<p>If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.</p>"""
    statistical_threshold: NotRequired[
        "aws_sdk_iot.types.statistical_threshold.StatisticalThreshold"
    ]
    """<p>A statistical ranking (percentile)that indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.</p>"""
    ml_detection_config: NotRequired[
        "aws_sdk_iot.types.machine_learning_detection_config.MachineLearningDetectionConfig"
    ]
    """<p> The configuration of an ML Detect </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BehaviorCriteria) -> dict:
    out: dict = {}
    if "comparison_operator" in value:
        import aws_sdk_iot.types.comparison_operator

        out["comparisonOperator"] = (
            aws_sdk_iot.types.comparison_operator.serialize_json(
                value["comparison_operator"]
            )
        )
    if "value" in value:
        import aws_sdk_iot.types.metric_value

        out["value"] = aws_sdk_iot.types.metric_value.serialize_json(value["value"])
    if "duration_seconds" in value:
        out["durationSeconds"] = value["duration_seconds"]
    if "consecutive_datapoints_to_alarm" in value:
        out["consecutiveDatapointsToAlarm"] = value["consecutive_datapoints_to_alarm"]
    if "consecutive_datapoints_to_clear" in value:
        out["consecutiveDatapointsToClear"] = value["consecutive_datapoints_to_clear"]
    if "statistical_threshold" in value:
        import aws_sdk_iot.types.statistical_threshold

        out["statisticalThreshold"] = (
            aws_sdk_iot.types.statistical_threshold.serialize_json(
                value["statistical_threshold"]
            )
        )
    if "ml_detection_config" in value:
        import aws_sdk_iot.types.machine_learning_detection_config

        out["mlDetectionConfig"] = (
            aws_sdk_iot.types.machine_learning_detection_config.serialize_json(
                value["ml_detection_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> BehaviorCriteria:
    out: BehaviorCriteria = {}  # type: ignore[typeddict-item]
    if "comparisonOperator" in data:
        import aws_sdk_iot.types.comparison_operator

        out["comparison_operator"] = (
            aws_sdk_iot.types.comparison_operator.deserialize_json(
                data["comparisonOperator"]
            )
        )
    if "value" in data:
        import aws_sdk_iot.types.metric_value

        out["value"] = aws_sdk_iot.types.metric_value.deserialize_json(data["value"])
    if "durationSeconds" in data:
        out["duration_seconds"] = data["durationSeconds"]
    if "consecutiveDatapointsToAlarm" in data:
        out["consecutive_datapoints_to_alarm"] = data["consecutiveDatapointsToAlarm"]
    if "consecutiveDatapointsToClear" in data:
        out["consecutive_datapoints_to_clear"] = data["consecutiveDatapointsToClear"]
    if "statisticalThreshold" in data:
        import aws_sdk_iot.types.statistical_threshold

        out["statistical_threshold"] = (
            aws_sdk_iot.types.statistical_threshold.deserialize_json(
                data["statisticalThreshold"]
            )
        )
    if "mlDetectionConfig" in data:
        import aws_sdk_iot.types.machine_learning_detection_config

        out["ml_detection_config"] = (
            aws_sdk_iot.types.machine_learning_detection_config.deserialize_json(
                data["mlDetectionConfig"]
            )
        )
    return out
