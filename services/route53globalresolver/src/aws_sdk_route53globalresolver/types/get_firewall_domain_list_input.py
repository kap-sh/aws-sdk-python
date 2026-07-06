"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetFirewallDomainListInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class GetFirewallDomainListInput(TypedDict, closed=True):
    firewall_domain_list_id: (
        "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    )
    """<p>ID of the domain list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFirewallDomainListInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFirewallDomainListInput:
    out: GetFirewallDomainListInput = {}  # type: ignore[typeddict-item]
    return out
