"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchDeleteFirewallRuleOutputItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_output_item

BatchDeleteFirewallRuleOutputItems: TypeAlias = list[
    "aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_output_item.BatchDeleteFirewallRuleOutputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteFirewallRuleOutputItems) -> list:
    import aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_output_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_output_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteFirewallRuleOutputItems:
    import aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_output_item

    out: BatchDeleteFirewallRuleOutputItems = []
    for item in data:
        out.append(
            aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_output_item.deserialize_json(
                item
            )
        )
    return out
