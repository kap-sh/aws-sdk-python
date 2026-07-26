"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleGroupAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_rule_group_association

FirewallRuleGroupAssociations: TypeAlias = list[
    "capo_route53resolver.types.firewall_rule_group_association.FirewallRuleGroupAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleGroupAssociations) -> list:
    import capo_route53resolver.types.firewall_rule_group_association

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.firewall_rule_group_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FirewallRuleGroupAssociations:
    import capo_route53resolver.types.firewall_rule_group_association

    out: FirewallRuleGroupAssociations = []
    for item in data:
        out.append(
            capo_route53resolver.types.firewall_rule_group_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
