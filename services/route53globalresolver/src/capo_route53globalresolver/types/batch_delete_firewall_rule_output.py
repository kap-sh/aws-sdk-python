"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchDeleteFirewallRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.batch_delete_firewall_rule_output_items


class BatchDeleteFirewallRuleOutput(TypedDict, closed=True):
    failures: "capo_route53globalresolver.types.batch_delete_firewall_rule_output_items.BatchDeleteFirewallRuleOutputItems"
    """<p>High level information about the DNS Firewall rules that failed to delete.</p>"""
    successes: "capo_route53globalresolver.types.batch_delete_firewall_rule_output_items.BatchDeleteFirewallRuleOutputItems"
    """<p>High level information about the DNS Firewall rules that were deleted successfully.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteFirewallRuleOutput) -> dict:
    out: dict = {}
    import capo_route53globalresolver.types.batch_delete_firewall_rule_output_items

    out["failures"] = (
        capo_route53globalresolver.types.batch_delete_firewall_rule_output_items.serialize_json(
            value["failures"]
        )
    )
    import capo_route53globalresolver.types.batch_delete_firewall_rule_output_items

    out["successes"] = (
        capo_route53globalresolver.types.batch_delete_firewall_rule_output_items.serialize_json(
            value["successes"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteFirewallRuleOutput:
    out: BatchDeleteFirewallRuleOutput = {}  # type: ignore[typeddict-item]
    if "failures" in data:
        import capo_route53globalresolver.types.batch_delete_firewall_rule_output_items

        out["failures"] = (
            capo_route53globalresolver.types.batch_delete_firewall_rule_output_items.deserialize_json(
                data["failures"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteFirewallRuleOutput.failures required")
    if "successes" in data:
        import capo_route53globalresolver.types.batch_delete_firewall_rule_output_items

        out["successes"] = (
            capo_route53globalresolver.types.batch_delete_firewall_rule_output_items.deserialize_json(
                data["successes"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteFirewallRuleOutput.successes required")
    return out
