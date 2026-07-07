"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetFirewallRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class GetFirewallRuleInput(TypedDict, closed=True):
    firewall_rule_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the DNS Firewall rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFirewallRuleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFirewallRuleInput:
    out: GetFirewallRuleInput = {}  # type: ignore[typeddict-item]
    return out
