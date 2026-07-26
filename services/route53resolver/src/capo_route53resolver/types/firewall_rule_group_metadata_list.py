"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleGroupMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_rule_group_metadata

FirewallRuleGroupMetadataList: TypeAlias = list[
    "capo_route53resolver.types.firewall_rule_group_metadata.FirewallRuleGroupMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleGroupMetadataList) -> list:
    import capo_route53resolver.types.firewall_rule_group_metadata

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.firewall_rule_group_metadata.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FirewallRuleGroupMetadataList:
    import capo_route53resolver.types.firewall_rule_group_metadata

    out: FirewallRuleGroupMetadataList = []
    for item in data:
        out.append(
            capo_route53resolver.types.firewall_rule_group_metadata.deserialize_aws_json_1_1(
                item
            )
        )
    return out
