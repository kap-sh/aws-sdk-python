"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListManagedFirewallDomainListsInput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListManagedFirewallDomainListsInput(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to retrieve in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response.</p>"""
    managed_firewall_domain_list_type: "str"
    """<p>The category of the Manage DNS list either <code>THREAT</code> or <code>CONTENT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedFirewallDomainListsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedFirewallDomainListsInput:
    out: ListManagedFirewallDomainListsInput = {}  # type: ignore[typeddict-item]
    return out
