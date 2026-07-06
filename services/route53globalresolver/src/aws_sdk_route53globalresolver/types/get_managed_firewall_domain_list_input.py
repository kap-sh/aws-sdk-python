"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetManagedFirewallDomainListInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class GetManagedFirewallDomainListInput(TypedDict, closed=True):
    managed_firewall_domain_list_id: (
        "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    )
    """<p>ID of the Managed Domain List.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedFirewallDomainListInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetManagedFirewallDomainListInput:
    out: GetManagedFirewallDomainListInput = {}  # type: ignore[typeddict-item]
    return out
