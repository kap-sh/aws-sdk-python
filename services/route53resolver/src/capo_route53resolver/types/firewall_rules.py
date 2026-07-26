"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_rule

FirewallRules: TypeAlias = list["capo_route53resolver.types.firewall_rule.FirewallRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRules) -> list:
    import capo_route53resolver.types.firewall_rule

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.firewall_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FirewallRules:
    import capo_route53resolver.types.firewall_rule

    out: FirewallRules = []
    for item in data:
        out.append(
            capo_route53resolver.types.firewall_rule.deserialize_aws_json_1_1(item)
        )
    return out
