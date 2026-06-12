"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteFirewallRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class DeleteFirewallRuleInput(TypedDict):
    firewall_rule_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the firewall rule to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFirewallRuleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFirewallRuleInput:
    out: DeleteFirewallRuleInput = {}  # type: ignore[typeddict-item]
    return out
