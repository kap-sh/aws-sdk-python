"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAlarmsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.composite_alarms
    import aws_sdk_cloudwatch.types.metric_alarms
    import aws_sdk_cloudwatch.types.next_token


class DescribeAlarmsOutput(TypedDict, closed=True):
    composite_alarms: NotRequired[
        "aws_sdk_cloudwatch.types.composite_alarms.CompositeAlarms"
    ]
    """<p>The information about any composite alarms returned by the operation.</p>"""
    metric_alarms: NotRequired["aws_sdk_cloudwatch.types.metric_alarms.MetricAlarms"]
    """<p>The information about any metric alarms returned by the operation.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch.types.next_token.NextToken"]
    """<p>The token that marks the start of the next batch of returned results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAlarmsOutput) -> dict:
    out: dict = {}
    if "composite_alarms" in value:
        import aws_sdk_cloudwatch.types.composite_alarms

        out["CompositeAlarms"] = (
            aws_sdk_cloudwatch.types.composite_alarms.serialize_aws_json_1_0(
                value["composite_alarms"]
            )
        )
    if "metric_alarms" in value:
        import aws_sdk_cloudwatch.types.metric_alarms

        out["MetricAlarms"] = (
            aws_sdk_cloudwatch.types.metric_alarms.serialize_aws_json_1_0(
                value["metric_alarms"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAlarmsOutput:
    out: DescribeAlarmsOutput = {}  # type: ignore[typeddict-item]
    if "CompositeAlarms" in data:
        import aws_sdk_cloudwatch.types.composite_alarms

        out["composite_alarms"] = (
            aws_sdk_cloudwatch.types.composite_alarms.deserialize_aws_json_1_0(
                data["CompositeAlarms"]
            )
        )
    if "MetricAlarms" in data:
        import aws_sdk_cloudwatch.types.metric_alarms

        out["metric_alarms"] = (
            aws_sdk_cloudwatch.types.metric_alarms.deserialize_aws_json_1_0(
                data["MetricAlarms"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAlarmsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "composite_alarms" in value:
        import aws_sdk_cloudwatch.types.composite_alarms

        aws_sdk_cloudwatch.types.composite_alarms.serialize_query(
            value["composite_alarms"], pairs, f"{prefix}.CompositeAlarms"
        )
    if "metric_alarms" in value:
        import aws_sdk_cloudwatch.types.metric_alarms

        aws_sdk_cloudwatch.types.metric_alarms.serialize_query(
            value["metric_alarms"], pairs, f"{prefix}.MetricAlarms"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAlarmsOutput:
    out: DescribeAlarmsOutput = {}  # type: ignore[typeddict-item]
    child_composite_alarms = el.find("CompositeAlarms")
    if child_composite_alarms is not None:
        import aws_sdk_cloudwatch.types.composite_alarms

        out["composite_alarms"] = (
            aws_sdk_cloudwatch.types.composite_alarms.deserialize_query(
                child_composite_alarms
            )
        )
    child_metric_alarms = el.find("MetricAlarms")
    if child_metric_alarms is not None:
        import aws_sdk_cloudwatch.types.metric_alarms

        out["metric_alarms"] = aws_sdk_cloudwatch.types.metric_alarms.deserialize_query(
            child_metric_alarms
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
