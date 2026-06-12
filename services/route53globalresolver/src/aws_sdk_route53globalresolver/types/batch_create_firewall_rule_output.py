"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchCreateFirewallRuleOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output_items


class BatchCreateFirewallRuleOutput(TypedDict):
    failures: "aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output_items.BatchCreateFirewallRuleOutputItems"
    """<p>High level information about the DNS Firewall rules that failed to create.</p>"""
    successes: "aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output_items.BatchCreateFirewallRuleOutputItems"
    """<p>High level information about the DNS Firewall rules that were created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateFirewallRuleOutput) -> dict:
    out: dict = {}
    import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output_items

    out["failures"] = (
        aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output_items.serialize_json(
            value["failures"]
        )
    )
    import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output_items

    out["successes"] = (
        aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output_items.serialize_json(
            value["successes"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateFirewallRuleOutput:
    out: BatchCreateFirewallRuleOutput = {}  # type: ignore[typeddict-item]
    if "failures" in data:
        import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output_items

        out["failures"] = (
            aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output_items.deserialize_json(
                data["failures"]
            )
        )
    else:
        raise DeserializationError("BatchCreateFirewallRuleOutput.failures required")
    if "successes" in data:
        import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output_items

        out["successes"] = (
            aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output_items.deserialize_json(
                data["successes"]
            )
        )
    else:
        raise DeserializationError("BatchCreateFirewallRuleOutput.successes required")
    return out
