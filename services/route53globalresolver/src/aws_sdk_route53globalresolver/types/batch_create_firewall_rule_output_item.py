"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchCreateFirewallRuleOutputItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_result


class BatchCreateFirewallRuleOutputItem(TypedDict):
    firewall_rule: "aws_sdk_route53globalresolver.types.batch_create_firewall_rule_result.BatchCreateFirewallRuleResult"
    """<p>The firewall rule that was created in the batch operation.</p>"""
    code: "int"
    """<p>The HTTP response code for the batch operation result.</p>"""
    message: NotRequired["str"]
    """<p>A message describing the result of the batch operation, including error details if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateFirewallRuleOutputItem) -> dict:
    out: dict = {}
    import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_result

    out["firewallRule"] = (
        aws_sdk_route53globalresolver.types.batch_create_firewall_rule_result.serialize_json(
            value["firewall_rule"]
        )
    )
    out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchCreateFirewallRuleOutputItem:
    out: BatchCreateFirewallRuleOutputItem = {}  # type: ignore[typeddict-item]
    if "firewallRule" in data:
        import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_result

        out["firewall_rule"] = (
            aws_sdk_route53globalresolver.types.batch_create_firewall_rule_result.deserialize_json(
                data["firewallRule"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateFirewallRuleOutputItem.firewall_rule required"
        )
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("BatchCreateFirewallRuleOutputItem.code required")
    if "message" in data:
        out["message"] = data["message"]
    return out
