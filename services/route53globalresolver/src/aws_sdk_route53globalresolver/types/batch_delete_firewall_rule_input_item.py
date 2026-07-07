"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BatchDeleteFirewallRuleInputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class BatchDeleteFirewallRuleInputItem(TypedDict, closed=True):
    firewall_rule_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS Firewall rule to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteFirewallRuleInputItem) -> dict:
    out: dict = {}
    out["firewallRuleId"] = value["firewall_rule_id"]
    return out


def deserialize_json(data: dict) -> BatchDeleteFirewallRuleInputItem:
    out: BatchDeleteFirewallRuleInputItem = {}  # type: ignore[typeddict-item]
    if "firewallRuleId" in data:
        out["firewall_rule_id"] = data["firewallRuleId"]
    else:
        raise DeserializationError(
            "BatchDeleteFirewallRuleInputItem.firewall_rule_id required"
        )
    return out
