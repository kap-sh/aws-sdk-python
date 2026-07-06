"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchCreateFirewallRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input_items


class BatchCreateFirewallRuleInput(TypedDict, closed=True):
    firewall_rules: "aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input_items.BatchCreateFirewallRuleInputItems"
    """<p>The <code>BatchCreateFirewallRuleInputItem</code> objects contain the information for each Firewall rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateFirewallRuleInput) -> dict:
    out: dict = {}
    import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input_items

    out["firewallRules"] = (
        aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input_items.serialize_json(
            value["firewall_rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateFirewallRuleInput:
    out: BatchCreateFirewallRuleInput = {}  # type: ignore[typeddict-item]
    if "firewallRules" in data:
        import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input_items

        out["firewall_rules"] = (
            aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input_items.deserialize_json(
                data["firewallRules"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateFirewallRuleInput.firewall_rules required"
        )
    return out
