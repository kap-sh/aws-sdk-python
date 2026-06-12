"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListManagedInsightRulesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.managed_rule_descriptions
    import aws_sdk_cloudwatch.types.next_token


class ListManagedInsightRulesOutput(TypedDict):
    managed_rules: NotRequired[
        "aws_sdk_cloudwatch.types.managed_rule_descriptions.ManagedRuleDescriptions"
    ]
    """<p> The managed rules that are available for the specified Amazon Web Services resource. </p>"""
    next_token: NotRequired["aws_sdk_cloudwatch.types.next_token.NextToken"]
    """<p> Include this value to get the next set of rules if the value was returned by the previous operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListManagedInsightRulesOutput) -> dict:
    out: dict = {}
    if "managed_rules" in value:
        import aws_sdk_cloudwatch.types.managed_rule_descriptions

        out["ManagedRules"] = (
            aws_sdk_cloudwatch.types.managed_rule_descriptions.serialize_aws_json_1_0(
                value["managed_rules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListManagedInsightRulesOutput:
    out: ListManagedInsightRulesOutput = {}  # type: ignore[typeddict-item]
    if "ManagedRules" in data:
        import aws_sdk_cloudwatch.types.managed_rule_descriptions

        out["managed_rules"] = (
            aws_sdk_cloudwatch.types.managed_rule_descriptions.deserialize_aws_json_1_0(
                data["ManagedRules"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListManagedInsightRulesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "managed_rules" in value:
        import aws_sdk_cloudwatch.types.managed_rule_descriptions

        aws_sdk_cloudwatch.types.managed_rule_descriptions.serialize_query(
            value["managed_rules"], pairs, f"{prefix}.ManagedRules"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListManagedInsightRulesOutput:
    out: ListManagedInsightRulesOutput = {}  # type: ignore[typeddict-item]
    child_managed_rules = el.find("ManagedRules")
    if child_managed_rules is not None:
        import aws_sdk_cloudwatch.types.managed_rule_descriptions

        out["managed_rules"] = (
            aws_sdk_cloudwatch.types.managed_rule_descriptions.deserialize_query(
                child_managed_rules
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
