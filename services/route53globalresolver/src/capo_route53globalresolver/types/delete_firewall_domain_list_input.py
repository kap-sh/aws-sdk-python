"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteFirewallDomainListInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.resource_id


class DeleteFirewallDomainListInput(TypedDict, closed=True):
    firewall_domain_list_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the firewall domain list to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFirewallDomainListInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFirewallDomainListInput:
    out: DeleteFirewallDomainListInput = {}  # type: ignore[typeddict-item]
    return out
