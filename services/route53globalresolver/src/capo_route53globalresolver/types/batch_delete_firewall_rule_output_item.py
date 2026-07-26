"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchDeleteFirewallRuleOutputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.batch_delete_firewall_rule_result


class BatchDeleteFirewallRuleOutputItem(TypedDict, closed=True):
    firewall_rule: "capo_route53globalresolver.types.batch_delete_firewall_rule_result.BatchDeleteFirewallRuleResult"
    """<p>The firewall rule that was deleted in the batch operation.</p>"""
    code: "int"
    """<p>The response code for the delete operation.</p>"""
    message: NotRequired["str"]
    """<p>The response message for the delete operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteFirewallRuleOutputItem) -> dict:
    out: dict = {}
    import capo_route53globalresolver.types.batch_delete_firewall_rule_result

    out["firewallRule"] = (
        capo_route53globalresolver.types.batch_delete_firewall_rule_result.serialize_json(
            value["firewall_rule"]
        )
    )
    out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchDeleteFirewallRuleOutputItem:
    out: BatchDeleteFirewallRuleOutputItem = {}  # type: ignore[typeddict-item]
    if "firewallRule" in data:
        import capo_route53globalresolver.types.batch_delete_firewall_rule_result

        out["firewall_rule"] = (
            capo_route53globalresolver.types.batch_delete_firewall_rule_result.deserialize_json(
                data["firewallRule"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteFirewallRuleOutputItem.firewall_rule required"
        )
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("BatchDeleteFirewallRuleOutputItem.code required")
    if "message" in data:
        out["message"] = data["message"]
    return out
