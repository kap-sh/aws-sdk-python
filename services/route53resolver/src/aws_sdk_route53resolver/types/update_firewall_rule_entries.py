"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateFirewallRuleEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.update_firewall_rule_entry

UpdateFirewallRuleEntries: TypeAlias = list[
    "aws_sdk_route53resolver.types.update_firewall_rule_entry.UpdateFirewallRuleEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFirewallRuleEntries) -> list:
    import aws_sdk_route53resolver.types.update_firewall_rule_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53resolver.types.update_firewall_rule_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UpdateFirewallRuleEntries:
    import aws_sdk_route53resolver.types.update_firewall_rule_entry

    out: UpdateFirewallRuleEntries = []
    for item in data:
        out.append(
            aws_sdk_route53resolver.types.update_firewall_rule_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
