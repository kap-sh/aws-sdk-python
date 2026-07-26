"""Generated from Smithy shape ``com.amazonaws.emr#CloudWatchAlarmDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.comparison_operator
    import capo_emr.types.integer
    import capo_emr.types.metric_dimension_list
    import capo_emr.types.non_negative_double
    import capo_emr.types.statistic
    import capo_emr.types.string
    import capo_emr.types.unit


class CloudWatchAlarmDefinition(TypedDict, closed=True):
    comparison_operator: NotRequired[
        "capo_emr.types.comparison_operator.ComparisonOperator"
    ]
    """<p>Determines how the metric specified by <code>MetricName</code> is compared to the value specified by <code>Threshold</code>.</p>"""
    evaluation_periods: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is <code>1</code>.</p>"""
    metric_name: NotRequired["capo_emr.types.string.String"]
    """<p>The name of the CloudWatch metric that is watched to determine an alarm condition.</p>"""
    namespace: NotRequired["capo_emr.types.string.String"]
    """<p>The namespace for the CloudWatch metric. The default is <code>AWS/ElasticMapReduce</code>.</p>"""
    period: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The period, in seconds, over which the statistic is applied. CloudWatch metrics for Amazon EMR are emitted every five minutes (300 seconds), so if you specify a CloudWatch metric, specify <code>300</code>.</p>"""
    statistic: NotRequired["capo_emr.types.statistic.Statistic"]
    """<p>The statistic to apply to the metric associated with the alarm. The default is <code>AVERAGE</code>.</p>"""
    threshold: NotRequired["capo_emr.types.non_negative_double.NonNegativeDouble"]
    """<p>The value against which the specified statistic is compared.</p>"""
    unit: NotRequired["capo_emr.types.unit.Unit"]
    """<p>The unit of measure associated with the CloudWatch metric being watched. The value specified for <code>Unit</code> must correspond to the units specified in the CloudWatch metric.</p>"""
    dimensions: NotRequired["capo_emr.types.metric_dimension_list.MetricDimensionList"]
    """<p>A CloudWatch metric dimension.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchAlarmDefinition) -> dict:
    out: dict = {}
    if "comparison_operator" in value:
        import capo_emr.types.comparison_operator

        out["ComparisonOperator"] = (
            capo_emr.types.comparison_operator.serialize_aws_json_1_1(
                value["comparison_operator"]
            )
        )
    if "evaluation_periods" in value:
        out["EvaluationPeriods"] = value["evaluation_periods"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "period" in value:
        out["Period"] = value["period"]
    if "statistic" in value:
        import capo_emr.types.statistic

        out["Statistic"] = capo_emr.types.statistic.serialize_aws_json_1_1(
            value["statistic"]
        )
    if "threshold" in value:
        out["Threshold"] = value["threshold"]
    if "unit" in value:
        import capo_emr.types.unit

        out["Unit"] = capo_emr.types.unit.serialize_aws_json_1_1(value["unit"])
    if "dimensions" in value:
        import capo_emr.types.metric_dimension_list

        out["Dimensions"] = capo_emr.types.metric_dimension_list.serialize_aws_json_1_1(
            value["dimensions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchAlarmDefinition:
    out: CloudWatchAlarmDefinition = {}  # type: ignore[typeddict-item]
    if "ComparisonOperator" in data:
        import capo_emr.types.comparison_operator

        out["comparison_operator"] = (
            capo_emr.types.comparison_operator.deserialize_aws_json_1_1(
                data["ComparisonOperator"]
            )
        )
    if "EvaluationPeriods" in data:
        out["evaluation_periods"] = data["EvaluationPeriods"]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "Period" in data:
        out["period"] = data["Period"]
    if "Statistic" in data:
        import capo_emr.types.statistic

        out["statistic"] = capo_emr.types.statistic.deserialize_aws_json_1_1(
            data["Statistic"]
        )
    if "Threshold" in data:
        out["threshold"] = data["Threshold"]
    if "Unit" in data:
        import capo_emr.types.unit

        out["unit"] = capo_emr.types.unit.deserialize_aws_json_1_1(data["Unit"])
    if "Dimensions" in data:
        import capo_emr.types.metric_dimension_list

        out["dimensions"] = (
            capo_emr.types.metric_dimension_list.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    return out
