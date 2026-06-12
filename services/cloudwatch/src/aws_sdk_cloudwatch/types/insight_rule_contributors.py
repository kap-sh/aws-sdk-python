"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRuleContributors``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.insight_rule_contributor

InsightRuleContributors: TypeAlias = list[
    "aws_sdk_cloudwatch.types.insight_rule_contributor.InsightRuleContributor"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRuleContributors, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.insight_rule_contributor

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.insight_rule_contributor.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InsightRuleContributors:
    import aws_sdk_cloudwatch.types.insight_rule_contributor

    out: InsightRuleContributors = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudwatch.types.insight_rule_contributor.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: InsightRuleContributors, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.insight_rule_contributor

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.insight_rule_contributor.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> InsightRuleContributors:
    import aws_sdk_cloudwatch.types.insight_rule_contributor

    out: InsightRuleContributors = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudwatch.types.insight_rule_contributor.deserialize_query(child)
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRuleContributors) -> list:
    import aws_sdk_cloudwatch.types.insight_rule_contributor

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch.types.insight_rule_contributor.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InsightRuleContributors:
    import aws_sdk_cloudwatch.types.insight_rule_contributor

    out: InsightRuleContributors = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch.types.insight_rule_contributor.deserialize_aws_json_1_0(
                item
            )
        )
    return out
