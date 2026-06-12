"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleTypeDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.display_name
    import aws_sdk_route53resolver.types.rule_type_description
    import aws_sdk_route53resolver.types.rule_type_name
    import aws_sdk_route53resolver.types.rule_type_value


class FirewallRuleTypeDefinition(TypedDict):
    rule_type: NotRequired["aws_sdk_route53resolver.types.rule_type_name.RuleTypeName"]
    """<p>The category or class of the rule type, such as <code>FirewallAdvancedContentCategory</code> or <code>FirewallAdvancedThreatCategory</code>.</p>"""
    value: NotRequired["aws_sdk_route53resolver.types.rule_type_value.RuleTypeValue"]
    """<p>The specific identifier within the rule type category, such as <code>VIOLENCE_AND_HATE_SPEECH</code> or <code>PHISHING</code>.</p>"""
    display_name: NotRequired["aws_sdk_route53resolver.types.display_name.DisplayName"]
    """<p>The display name of the rule type.</p>"""
    description: NotRequired[
        "aws_sdk_route53resolver.types.rule_type_description.RuleTypeDescription"
    ]
    """<p>A description of the rule type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleTypeDefinition) -> dict:
    out: dict = {}
    if "rule_type" in value:
        out["RuleType"] = value["rule_type"]
    if "value" in value:
        out["Value"] = value["value"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallRuleTypeDefinition:
    out: FirewallRuleTypeDefinition = {}  # type: ignore[typeddict-item]
    if "RuleType" in data:
        out["rule_type"] = data["RuleType"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
