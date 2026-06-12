"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchUpdateFirewallRuleOutputItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_result


class BatchUpdateFirewallRuleOutputItem(TypedDict):
    firewall_rule: "aws_sdk_route53globalresolver.types.batch_update_firewall_rule_result.BatchUpdateFirewallRuleResult"
    """<p>The firewall rule that was updated in the batch operation.</p>"""
    code: "int"
    """<p>The response code for the update operation.</p>"""
    message: NotRequired["str"]
    """<p>The response message for the update operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFirewallRuleOutputItem) -> dict:
    out: dict = {}
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_result

    out["firewallRule"] = (
        aws_sdk_route53globalresolver.types.batch_update_firewall_rule_result.serialize_json(
            value["firewall_rule"]
        )
    )
    out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateFirewallRuleOutputItem:
    out: BatchUpdateFirewallRuleOutputItem = {}  # type: ignore[typeddict-item]
    if "firewallRule" in data:
        import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_result

        out["firewall_rule"] = (
            aws_sdk_route53globalresolver.types.batch_update_firewall_rule_result.deserialize_json(
                data["firewallRule"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateFirewallRuleOutputItem.firewall_rule required"
        )
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("BatchUpdateFirewallRuleOutputItem.code required")
    if "message" in data:
        out["message"] = data["message"]
    return out
