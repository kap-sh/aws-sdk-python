"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchUpdateFirewallRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_items


class BatchUpdateFirewallRuleInput(TypedDict, closed=True):
    firewall_rules: "aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_items.BatchUpdateFirewallRuleInputItems"
    """<p>The DNS Firewall rule IDs to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFirewallRuleInput) -> dict:
    out: dict = {}
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_items

    out["firewallRules"] = (
        aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_items.serialize_json(
            value["firewall_rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateFirewallRuleInput:
    out: BatchUpdateFirewallRuleInput = {}  # type: ignore[typeddict-item]
    if "firewallRules" in data:
        import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_items

        out["firewall_rules"] = (
            aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_items.deserialize_json(
                data["firewallRules"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateFirewallRuleInput.firewall_rules required"
        )
    return out
