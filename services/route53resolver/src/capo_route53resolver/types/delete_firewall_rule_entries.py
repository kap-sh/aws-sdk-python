"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteFirewallRuleEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.delete_firewall_rule_entry

DeleteFirewallRuleEntries: TypeAlias = list[
    "capo_route53resolver.types.delete_firewall_rule_entry.DeleteFirewallRuleEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFirewallRuleEntries) -> list:
    import capo_route53resolver.types.delete_firewall_rule_entry

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.delete_firewall_rule_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeleteFirewallRuleEntries:
    import capo_route53resolver.types.delete_firewall_rule_entry

    out: DeleteFirewallRuleEntries = []
    for item in data:
        out.append(
            capo_route53resolver.types.delete_firewall_rule_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
