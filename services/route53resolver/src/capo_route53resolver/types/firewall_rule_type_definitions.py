"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleTypeDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_rule_type_definition

FirewallRuleTypeDefinitions: TypeAlias = list[
    "capo_route53resolver.types.firewall_rule_type_definition.FirewallRuleTypeDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleTypeDefinitions) -> list:
    import capo_route53resolver.types.firewall_rule_type_definition

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.firewall_rule_type_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FirewallRuleTypeDefinitions:
    import capo_route53resolver.types.firewall_rule_type_definition

    out: FirewallRuleTypeDefinitions = []
    for item in data:
        out.append(
            capo_route53resolver.types.firewall_rule_type_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
