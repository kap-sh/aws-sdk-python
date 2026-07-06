"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallAdvancedThreatCategoryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_advanced_threat_category_value


class FirewallAdvancedThreatCategoryConfig(TypedDict, closed=True):
    category: "aws_sdk_route53resolver.types.firewall_advanced_threat_category_value.FirewallAdvancedThreatCategoryValue"
    """<p>The threat category identifier. To retrieve the list of available threat categories, call <a>ListFirewallRuleTypes</a> with <code>RuleType</code> set to <code>FirewallAdvancedThreatCategory</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallAdvancedThreatCategoryConfig) -> dict:
    out: dict = {}
    out["Category"] = value["category"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallAdvancedThreatCategoryConfig:
    out: FirewallAdvancedThreatCategoryConfig = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        out["category"] = data["Category"]
    else:
        raise DeserializationError(
            "FirewallAdvancedThreatCategoryConfig.category required"
        )
    return out
