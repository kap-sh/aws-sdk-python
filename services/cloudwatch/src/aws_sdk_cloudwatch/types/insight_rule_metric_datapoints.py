"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRuleMetricDatapoints``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.insight_rule_metric_datapoint

InsightRuleMetricDatapoints: TypeAlias = list[
    "aws_sdk_cloudwatch.types.insight_rule_metric_datapoint.InsightRuleMetricDatapoint"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRuleMetricDatapoints, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.insight_rule_metric_datapoint

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.insight_rule_metric_datapoint.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InsightRuleMetricDatapoints:
    import aws_sdk_cloudwatch.types.insight_rule_metric_datapoint

    out: InsightRuleMetricDatapoints = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudwatch.types.insight_rule_metric_datapoint.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: InsightRuleMetricDatapoints, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.insight_rule_metric_datapoint

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.insight_rule_metric_datapoint.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> InsightRuleMetricDatapoints:
    import aws_sdk_cloudwatch.types.insight_rule_metric_datapoint

    out: InsightRuleMetricDatapoints = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudwatch.types.insight_rule_metric_datapoint.deserialize_query(
                child
            )
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRuleMetricDatapoints) -> list:
    import aws_sdk_cloudwatch.types.insight_rule_metric_datapoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch.types.insight_rule_metric_datapoint.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InsightRuleMetricDatapoints:
    import aws_sdk_cloudwatch.types.insight_rule_metric_datapoint

    out: InsightRuleMetricDatapoints = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch.types.insight_rule_metric_datapoint.deserialize_aws_json_1_0(
                item
            )
        )
    return out
