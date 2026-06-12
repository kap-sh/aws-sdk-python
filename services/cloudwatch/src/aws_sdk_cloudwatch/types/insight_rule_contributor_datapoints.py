"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRuleContributorDatapoints``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint

InsightRuleContributorDatapoints: TypeAlias = list[
    "aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint.InsightRuleContributorDatapoint"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRuleContributorDatapoints, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InsightRuleContributorDatapoints:
    import aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint

    out: InsightRuleContributorDatapoints = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: InsightRuleContributorDatapoints, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> InsightRuleContributorDatapoints:
    import aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint

    out: InsightRuleContributorDatapoints = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint.deserialize_query(
                child
            )
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRuleContributorDatapoints) -> list:
    import aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InsightRuleContributorDatapoints:
    import aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint

    out: InsightRuleContributorDatapoints = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch.types.insight_rule_contributor_datapoint.deserialize_aws_json_1_0(
                item
            )
        )
    return out
