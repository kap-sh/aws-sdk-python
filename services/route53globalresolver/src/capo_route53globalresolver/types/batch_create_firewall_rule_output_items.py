"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchCreateFirewallRuleOutputItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.batch_create_firewall_rule_output_item

BatchCreateFirewallRuleOutputItems: TypeAlias = list[
    "capo_route53globalresolver.types.batch_create_firewall_rule_output_item.BatchCreateFirewallRuleOutputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateFirewallRuleOutputItems) -> list:
    import capo_route53globalresolver.types.batch_create_firewall_rule_output_item

    out: list = []
    for item in value:
        out.append(
            capo_route53globalresolver.types.batch_create_firewall_rule_output_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateFirewallRuleOutputItems:
    import capo_route53globalresolver.types.batch_create_firewall_rule_output_item

    out: BatchCreateFirewallRuleOutputItems = []
    for item in data:
        out.append(
            capo_route53globalresolver.types.batch_create_firewall_rule_output_item.deserialize_json(
                item
            )
        )
    return out
