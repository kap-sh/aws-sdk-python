"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentMetricSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.metric_name
    import aws_sdk_sagemaker.types.optional_double
    import aws_sdk_sagemaker.types.optional_integer
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.trial_component_source_arn


class TrialComponentMetricSummary(TypedDict):
    metric_name: NotRequired["aws_sdk_sagemaker.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    source_arn: NotRequired[
        "aws_sdk_sagemaker.types.trial_component_source_arn.TrialComponentSourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the source.</p>"""
    time_stamp: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the metric was last updated.</p>"""
    max: NotRequired["aws_sdk_sagemaker.types.optional_double.OptionalDouble"]
    """<p>The maximum value of the metric.</p>"""
    min: NotRequired["aws_sdk_sagemaker.types.optional_double.OptionalDouble"]
    """<p>The minimum value of the metric.</p>"""
    last: NotRequired["aws_sdk_sagemaker.types.optional_double.OptionalDouble"]
    """<p>The most recent value of the metric.</p>"""
    count: NotRequired["aws_sdk_sagemaker.types.optional_integer.OptionalInteger"]
    """<p>The number of samples used to generate the metric.</p>"""
    avg: NotRequired["aws_sdk_sagemaker.types.optional_double.OptionalDouble"]
    """<p>The average value of the metric.</p>"""
    std_dev: NotRequired["aws_sdk_sagemaker.types.optional_double.OptionalDouble"]
    """<p>The standard deviation of the metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentMetricSummary) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "time_stamp" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["TimeStamp"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["time_stamp"]
        )
    if "max" in value:
        out["Max"] = value["max"]
    if "min" in value:
        out["Min"] = value["min"]
    if "last" in value:
        out["Last"] = value["last"]
    if "count" in value:
        out["Count"] = value["count"]
    if "avg" in value:
        out["Avg"] = value["avg"]
    if "std_dev" in value:
        out["StdDev"] = value["std_dev"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialComponentMetricSummary:
    out: TrialComponentMetricSummary = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "TimeStamp" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["time_stamp"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["TimeStamp"]
        )
    if "Max" in data:
        out["max"] = data["Max"]
    if "Min" in data:
        out["min"] = data["Min"]
    if "Last" in data:
        out["last"] = data["Last"]
    if "Count" in data:
        out["count"] = data["Count"]
    if "Avg" in data:
        out["avg"] = data["Avg"]
    if "StdDev" in data:
        out["std_dev"] = data["StdDev"]
    return out
