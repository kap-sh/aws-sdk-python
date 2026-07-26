"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchCreateFirewallRuleInputItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.batch_create_firewall_rule_input_item

BatchCreateFirewallRuleInputItems: TypeAlias = list[
    "capo_route53globalresolver.types.batch_create_firewall_rule_input_item.BatchCreateFirewallRuleInputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateFirewallRuleInputItems) -> list:
    import capo_route53globalresolver.types.batch_create_firewall_rule_input_item

    out: list = []
    for item in value:
        out.append(
            capo_route53globalresolver.types.batch_create_firewall_rule_input_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateFirewallRuleInputItems:
    import capo_route53globalresolver.types.batch_create_firewall_rule_input_item

    out: BatchCreateFirewallRuleInputItems = []
    for item in data:
        out.append(
            capo_route53globalresolver.types.batch_create_firewall_rule_input_item.deserialize_json(
                item
            )
        )
    return out
