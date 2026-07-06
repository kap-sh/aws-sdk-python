"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListFirewallDomainsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class ListFirewallDomainsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to retrieve in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response.</p>"""
    firewall_domain_list_id: (
        "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    )
    """<p>ID of the DNS Firewall domain list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFirewallDomainsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFirewallDomainsInput:
    out: ListFirewallDomainsInput = {}  # type: ignore[typeddict-item]
    return out
