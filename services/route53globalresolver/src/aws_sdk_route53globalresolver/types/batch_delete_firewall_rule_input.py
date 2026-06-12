"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchDeleteFirewallRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_items


class BatchDeleteFirewallRuleInput(TypedDict):
    firewall_rules: "aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_items.BatchDeleteFirewallRuleInputItems"
    """<p>An array of the DNS Firewall IDs to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteFirewallRuleInput) -> dict:
    out: dict = {}
    import aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_items

    out["firewallRules"] = (
        aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_items.serialize_json(
            value["firewall_rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteFirewallRuleInput:
    out: BatchDeleteFirewallRuleInput = {}  # type: ignore[typeddict-item]
    if "firewallRules" in data:
        import aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_items

        out["firewall_rules"] = (
            aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_items.deserialize_json(
                data["firewallRules"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteFirewallRuleInput.firewall_rules required"
        )
    return out
