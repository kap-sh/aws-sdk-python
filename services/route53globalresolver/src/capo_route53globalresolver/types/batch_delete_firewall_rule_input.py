"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchDeleteFirewallRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.batch_delete_firewall_rule_input_items


class BatchDeleteFirewallRuleInput(TypedDict, closed=True):
    firewall_rules: "capo_route53globalresolver.types.batch_delete_firewall_rule_input_items.BatchDeleteFirewallRuleInputItems"
    """<p>An array of the DNS Firewall IDs to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteFirewallRuleInput) -> dict:
    out: dict = {}
    import capo_route53globalresolver.types.batch_delete_firewall_rule_input_items

    out["firewallRules"] = (
        capo_route53globalresolver.types.batch_delete_firewall_rule_input_items.serialize_json(
            value["firewall_rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteFirewallRuleInput:
    out: BatchDeleteFirewallRuleInput = {}  # type: ignore[typeddict-item]
    if "firewallRules" in data:
        import capo_route53globalresolver.types.batch_delete_firewall_rule_input_items

        out["firewall_rules"] = (
            capo_route53globalresolver.types.batch_delete_firewall_rule_input_items.deserialize_json(
                data["firewallRules"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteFirewallRuleInput.firewall_rules required"
        )
    return out
