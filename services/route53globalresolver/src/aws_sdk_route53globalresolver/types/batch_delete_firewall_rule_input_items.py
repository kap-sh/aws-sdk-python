"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchDeleteFirewallRuleInputItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_item

BatchDeleteFirewallRuleInputItems: TypeAlias = list[
    "aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_item.BatchDeleteFirewallRuleInputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteFirewallRuleInputItems) -> list:
    import aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteFirewallRuleInputItems:
    import aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_item

    out: BatchDeleteFirewallRuleInputItems = []
    for item in data:
        out.append(
            aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_item.deserialize_json(
                item
            )
        )
    return out
