"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteInsightRulesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.insight_rule_names


class DeleteInsightRulesInput(TypedDict):
    rule_names: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_names.InsightRuleNames"
    ]
    """<p>An array of the rule names to delete. If you need to find out the names of your rules, use <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html\">DescribeInsightRules</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteInsightRulesInput) -> dict:
    out: dict = {}
    if "rule_names" in value:
        import aws_sdk_cloudwatch.types.insight_rule_names

        out["RuleNames"] = (
            aws_sdk_cloudwatch.types.insight_rule_names.serialize_aws_json_1_0(
                value["rule_names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteInsightRulesInput:
    out: DeleteInsightRulesInput = {}  # type: ignore[typeddict-item]
    if "RuleNames" in data:
        import aws_sdk_cloudwatch.types.insight_rule_names

        out["rule_names"] = (
            aws_sdk_cloudwatch.types.insight_rule_names.deserialize_aws_json_1_0(
                data["RuleNames"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteInsightRulesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rule_names" in value:
        import aws_sdk_cloudwatch.types.insight_rule_names

        aws_sdk_cloudwatch.types.insight_rule_names.serialize_query(
            value["rule_names"], pairs, f"{prefix}.RuleNames"
        )


def deserialize_query(el: Element) -> DeleteInsightRulesInput:
    out: DeleteInsightRulesInput = {}  # type: ignore[typeddict-item]
    child_rule_names = el.find("RuleNames")
    if child_rule_names is not None:
        import aws_sdk_cloudwatch.types.insight_rule_names

        out["rule_names"] = (
            aws_sdk_cloudwatch.types.insight_rule_names.deserialize_query(
                child_rule_names
            )
        )
    return out
