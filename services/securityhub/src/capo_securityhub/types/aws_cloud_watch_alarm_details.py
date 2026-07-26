"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudWatchAlarmDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_cloud_watch_alarm_dimensions_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.double
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsCloudWatchAlarmDetails(TypedDict, closed=True):
    actions_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether actions should be executed during any changes to the alarm state. </p>"""
    alarm_actions: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The list of actions, specified as Amazon Resource Names (ARNs) to execute when this alarm transitions into an <code>ALARM</code> state from any other state. </p>"""
    alarm_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the alarm. </p>"""
    alarm_configuration_updated_timestamp: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The time stamp of the last update to the alarm configuration. </p>"""
    alarm_description: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the alarm. </p>"""
    alarm_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the alarm. If you don't specify a name, CloudFront generates a unique physical ID and uses that ID for the alarm name. </p>"""
    comparison_operator: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand. </p>"""
    datapoints_to_alarm: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of datapoints that must be breaching to trigger the alarm. </p>"""
    dimensions: NotRequired[
        "capo_securityhub.types.aws_cloud_watch_alarm_dimensions_list.AwsCloudWatchAlarmDimensionsList"
    ]
    """<p>The dimensions for the metric associated with the alarm. </p>"""
    evaluate_low_sample_count_percentile: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Used only for alarms based on percentiles. If <code>ignore</code>, the alarm state does not change during periods with too few data points to be statistically significant. If <code>evaluate</code> or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available. </p>"""
    evaluation_periods: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of periods over which data is compared to the specified threshold. </p>"""
    extended_statistic: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The percentile statistic for the metric associated with the alarm. </p>"""
    insufficient_data_actions: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The actions to execute when this alarm transitions to the <code>INSUFFICIENT_DATA</code> state from any other state. Each action is specified as an ARN. </p>"""
    metric_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you use <code>Metrics</code> instead and you can't specify <code>MetricName</code>. </p>"""
    namespace: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The namespace of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you can't specify <code>Namespace</code> and you use <code>Metrics</code> instead. </p>"""
    ok_actions: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The actions to execute when this alarm transitions to the <code>OK</code> state from any other state. Each action is specified as an ARN. </p>"""
    period: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The period, in seconds, over which the statistic is applied. This is required for an alarm based on a metric. </p>"""
    statistic: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use <code>ExtendedStatistic</code>.</p> <p>For an alarm based on a metric, you must specify either <code>Statistic</code> or <code>ExtendedStatistic</code> but not both.</p> <p>For an alarm based on a math expression, you can't specify <code>Statistic</code>. Instead, you use <code>Metrics</code>.</p>"""
    threshold: NotRequired["capo_securityhub.types.double.Double"]
    """<p>The value to compare with the specified statistic. </p>"""
    threshold_metric_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>n an alarm based on an anomaly detection model, this is the ID of the <code>ANOMALY_DETECTION_BAND</code> function used as the threshold for the alarm. </p>"""
    treat_missing_data: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Sets how this alarm is to handle missing data points. </p>"""
    unit: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unit of the metric associated with the alarm. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudWatchAlarmDetails) -> dict:
    out: dict = {}
    if "actions_enabled" in value:
        out["ActionsEnabled"] = value["actions_enabled"]
    if "alarm_actions" in value:
        import capo_securityhub.types.non_empty_string_list

        out["AlarmActions"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["alarm_actions"]
            )
        )
    if "alarm_arn" in value:
        out["AlarmArn"] = value["alarm_arn"]
    if "alarm_configuration_updated_timestamp" in value:
        out["AlarmConfigurationUpdatedTimestamp"] = value[
            "alarm_configuration_updated_timestamp"
        ]
    if "alarm_description" in value:
        out["AlarmDescription"] = value["alarm_description"]
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "comparison_operator" in value:
        out["ComparisonOperator"] = value["comparison_operator"]
    if "datapoints_to_alarm" in value:
        out["DatapointsToAlarm"] = value["datapoints_to_alarm"]
    if "dimensions" in value:
        import capo_securityhub.types.aws_cloud_watch_alarm_dimensions_list

        out["Dimensions"] = (
            capo_securityhub.types.aws_cloud_watch_alarm_dimensions_list.serialize_json(
                value["dimensions"]
            )
        )
    if "evaluate_low_sample_count_percentile" in value:
        out["EvaluateLowSampleCountPercentile"] = value[
            "evaluate_low_sample_count_percentile"
        ]
    if "evaluation_periods" in value:
        out["EvaluationPeriods"] = value["evaluation_periods"]
    if "extended_statistic" in value:
        out["ExtendedStatistic"] = value["extended_statistic"]
    if "insufficient_data_actions" in value:
        import capo_securityhub.types.non_empty_string_list

        out["InsufficientDataActions"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["insufficient_data_actions"]
            )
        )
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "ok_actions" in value:
        import capo_securityhub.types.non_empty_string_list

        out["OkActions"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["ok_actions"]
        )
    if "period" in value:
        out["Period"] = value["period"]
    if "statistic" in value:
        out["Statistic"] = value["statistic"]
    if "threshold" in value:
        out["Threshold"] = value["threshold"]
    if "threshold_metric_id" in value:
        out["ThresholdMetricId"] = value["threshold_metric_id"]
    if "treat_missing_data" in value:
        out["TreatMissingData"] = value["treat_missing_data"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> AwsCloudWatchAlarmDetails:
    out: AwsCloudWatchAlarmDetails = {}  # type: ignore[typeddict-item]
    if "ActionsEnabled" in data:
        out["actions_enabled"] = data["ActionsEnabled"]
    if "AlarmActions" in data:
        import capo_securityhub.types.non_empty_string_list

        out["alarm_actions"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["AlarmActions"]
            )
        )
    if "AlarmArn" in data:
        out["alarm_arn"] = data["AlarmArn"]
    if "AlarmConfigurationUpdatedTimestamp" in data:
        out["alarm_configuration_updated_timestamp"] = data[
            "AlarmConfigurationUpdatedTimestamp"
        ]
    if "AlarmDescription" in data:
        out["alarm_description"] = data["AlarmDescription"]
    if "AlarmName" in data:
        out["alarm_name"] = data["AlarmName"]
    if "ComparisonOperator" in data:
        out["comparison_operator"] = data["ComparisonOperator"]
    if "DatapointsToAlarm" in data:
        out["datapoints_to_alarm"] = data["DatapointsToAlarm"]
    if "Dimensions" in data:
        import capo_securityhub.types.aws_cloud_watch_alarm_dimensions_list

        out["dimensions"] = (
            capo_securityhub.types.aws_cloud_watch_alarm_dimensions_list.deserialize_json(
                data["Dimensions"]
            )
        )
    if "EvaluateLowSampleCountPercentile" in data:
        out["evaluate_low_sample_count_percentile"] = data[
            "EvaluateLowSampleCountPercentile"
        ]
    if "EvaluationPeriods" in data:
        out["evaluation_periods"] = data["EvaluationPeriods"]
    if "ExtendedStatistic" in data:
        out["extended_statistic"] = data["ExtendedStatistic"]
    if "InsufficientDataActions" in data:
        import capo_securityhub.types.non_empty_string_list

        out["insufficient_data_actions"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["InsufficientDataActions"]
            )
        )
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "OkActions" in data:
        import capo_securityhub.types.non_empty_string_list

        out["ok_actions"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["OkActions"]
            )
        )
    if "Period" in data:
        out["period"] = data["Period"]
    if "Statistic" in data:
        out["statistic"] = data["Statistic"]
    if "Threshold" in data:
        out["threshold"] = data["Threshold"]
    if "ThresholdMetricId" in data:
        out["threshold_metric_id"] = data["ThresholdMetricId"]
    if "TreatMissingData" in data:
        out["treat_missing_data"] = data["TreatMissingData"]
    if "Unit" in data:
        out["unit"] = data["Unit"]
    return out
