"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchUpdateFirewallRuleOutputItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_output_item

BatchUpdateFirewallRuleOutputItems: TypeAlias = list[
    "aws_sdk_route53globalresolver.types.batch_update_firewall_rule_output_item.BatchUpdateFirewallRuleOutputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFirewallRuleOutputItems) -> list:
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_output_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53globalresolver.types.batch_update_firewall_rule_output_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateFirewallRuleOutputItems:
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_output_item

    out: BatchUpdateFirewallRuleOutputItems = []
    for item in data:
        out.append(
            aws_sdk_route53globalresolver.types.batch_update_firewall_rule_output_item.deserialize_json(
                item
            )
        )
    return out
