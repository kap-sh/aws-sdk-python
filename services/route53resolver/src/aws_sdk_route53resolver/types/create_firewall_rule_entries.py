"""Generated from Smithy shape ``com.amazonaws.route53resolver#CreateFirewallRuleEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.create_firewall_rule_entry

CreateFirewallRuleEntries: TypeAlias = list[
    "aws_sdk_route53resolver.types.create_firewall_rule_entry.CreateFirewallRuleEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFirewallRuleEntries) -> list:
    import aws_sdk_route53resolver.types.create_firewall_rule_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53resolver.types.create_firewall_rule_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CreateFirewallRuleEntries:
    import aws_sdk_route53resolver.types.create_firewall_rule_entry

    out: CreateFirewallRuleEntries = []
    for item in data:
        out.append(
            aws_sdk_route53resolver.types.create_firewall_rule_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
