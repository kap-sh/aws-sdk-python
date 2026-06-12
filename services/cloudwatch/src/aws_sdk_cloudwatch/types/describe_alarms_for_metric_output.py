"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAlarmsForMetricOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.metric_alarms


class DescribeAlarmsForMetricOutput(TypedDict):
    metric_alarms: NotRequired["aws_sdk_cloudwatch.types.metric_alarms.MetricAlarms"]
    """<p>The information for each alarm with the specified metric.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAlarmsForMetricOutput) -> dict:
    out: dict = {}
    if "metric_alarms" in value:
        import aws_sdk_cloudwatch.types.metric_alarms

        out["MetricAlarms"] = (
            aws_sdk_cloudwatch.types.metric_alarms.serialize_aws_json_1_0(
                value["metric_alarms"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAlarmsForMetricOutput:
    out: DescribeAlarmsForMetricOutput = {}  # type: ignore[typeddict-item]
    if "MetricAlarms" in data:
        import aws_sdk_cloudwatch.types.metric_alarms

        out["metric_alarms"] = (
            aws_sdk_cloudwatch.types.metric_alarms.deserialize_aws_json_1_0(
                data["MetricAlarms"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAlarmsForMetricOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "metric_alarms" in value:
        import aws_sdk_cloudwatch.types.metric_alarms

        aws_sdk_cloudwatch.types.metric_alarms.serialize_query(
            value["metric_alarms"], pairs, f"{prefix}.MetricAlarms"
        )


def deserialize_query(el: Element) -> DescribeAlarmsForMetricOutput:
    out: DescribeAlarmsForMetricOutput = {}  # type: ignore[typeddict-item]
    child_metric_alarms = el.find("MetricAlarms")
    if child_metric_alarms is not None:
        import aws_sdk_cloudwatch.types.metric_alarms

        out["metric_alarms"] = aws_sdk_cloudwatch.types.metric_alarms.deserialize_query(
            child_metric_alarms
        )
    return out
