"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchUpdateFirewallRuleInputItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_item

BatchUpdateFirewallRuleInputItems: TypeAlias = list[
    "aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_item.BatchUpdateFirewallRuleInputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFirewallRuleInputItems) -> list:
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateFirewallRuleInputItems:
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_item

    out: BatchUpdateFirewallRuleInputItems = []
    for item in data:
        out.append(
            aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_item.deserialize_json(
                item
            )
        )
    return out
