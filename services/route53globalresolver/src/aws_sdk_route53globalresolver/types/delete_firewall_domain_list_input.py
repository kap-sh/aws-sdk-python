"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteFirewallDomainListInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class DeleteFirewallDomainListInput(TypedDict):
    firewall_domain_list_id: (
        "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    )
    """<p>The unique identifier of the firewall domain list to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFirewallDomainListInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFirewallDomainListInput:
    out: DeleteFirewallDomainListInput = {}  # type: ignore[typeddict-item]
    return out
