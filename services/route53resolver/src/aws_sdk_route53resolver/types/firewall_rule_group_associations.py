"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleGroupAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_rule_group_association

FirewallRuleGroupAssociations: TypeAlias = list[
    "aws_sdk_route53resolver.types.firewall_rule_group_association.FirewallRuleGroupAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleGroupAssociations) -> list:
    import aws_sdk_route53resolver.types.firewall_rule_group_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53resolver.types.firewall_rule_group_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FirewallRuleGroupAssociations:
    import aws_sdk_route53resolver.types.firewall_rule_group_association

    out: FirewallRuleGroupAssociations = []
    for item in data:
        out.append(
            aws_sdk_route53resolver.types.firewall_rule_group_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
