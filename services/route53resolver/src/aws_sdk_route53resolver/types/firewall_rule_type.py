"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.dns_threat_protection_rule_type_config
    import aws_sdk_route53resolver.types.firewall_advanced_content_category_config
    import aws_sdk_route53resolver.types.firewall_advanced_threat_category_config


class FirewallRuleType(TypedDict):
    firewall_advanced_content_category: NotRequired[
        "aws_sdk_route53resolver.types.firewall_advanced_content_category_config.FirewallAdvancedContentCategoryConfig"
    ]
    """<p>The configuration for a content category-based filtering rule.</p>"""
    firewall_advanced_threat_category: NotRequired[
        "aws_sdk_route53resolver.types.firewall_advanced_threat_category_config.FirewallAdvancedThreatCategoryConfig"
    ]
    """<p>The configuration for a threat category-based filtering rule.</p>"""
    dns_threat_protection: NotRequired[
        "aws_sdk_route53resolver.types.dns_threat_protection_rule_type_config.DnsThreatProtectionRuleTypeConfig"
    ]
    """<p>The configuration for a DNS threat protection rule type, such as DGA or DNS tunneling detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleType) -> dict:
    out: dict = {}
    if "firewall_advanced_content_category" in value:
        import aws_sdk_route53resolver.types.firewall_advanced_content_category_config

        out["FirewallAdvancedContentCategory"] = (
            aws_sdk_route53resolver.types.firewall_advanced_content_category_config.serialize_aws_json_1_1(
                value["firewall_advanced_content_category"]
            )
        )
    if "firewall_advanced_threat_category" in value:
        import aws_sdk_route53resolver.types.firewall_advanced_threat_category_config

        out["FirewallAdvancedThreatCategory"] = (
            aws_sdk_route53resolver.types.firewall_advanced_threat_category_config.serialize_aws_json_1_1(
                value["firewall_advanced_threat_category"]
            )
        )
    if "dns_threat_protection" in value:
        import aws_sdk_route53resolver.types.dns_threat_protection_rule_type_config

        out["DnsThreatProtection"] = (
            aws_sdk_route53resolver.types.dns_threat_protection_rule_type_config.serialize_aws_json_1_1(
                value["dns_threat_protection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallRuleType:
    out: FirewallRuleType = {}  # type: ignore[typeddict-item]
    if "FirewallAdvancedContentCategory" in data:
        import aws_sdk_route53resolver.types.firewall_advanced_content_category_config

        out["firewall_advanced_content_category"] = (
            aws_sdk_route53resolver.types.firewall_advanced_content_category_config.deserialize_aws_json_1_1(
                data["FirewallAdvancedContentCategory"]
            )
        )
    if "FirewallAdvancedThreatCategory" in data:
        import aws_sdk_route53resolver.types.firewall_advanced_threat_category_config

        out["firewall_advanced_threat_category"] = (
            aws_sdk_route53resolver.types.firewall_advanced_threat_category_config.deserialize_aws_json_1_1(
                data["FirewallAdvancedThreatCategory"]
            )
        )
    if "DnsThreatProtection" in data:
        import aws_sdk_route53resolver.types.dns_threat_protection_rule_type_config

        out["dns_threat_protection"] = (
            aws_sdk_route53resolver.types.dns_threat_protection_rule_type_config.deserialize_aws_json_1_1(
                data["DnsThreatProtection"]
            )
        )
    return out
