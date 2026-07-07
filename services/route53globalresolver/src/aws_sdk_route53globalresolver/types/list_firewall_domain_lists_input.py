"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListFirewallDomainListsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class ListFirewallDomainListsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to retrieve in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response.</p>"""
    global_resolver_id: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the Global Resolver that contains the DNS view the domain lists are associated to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFirewallDomainListsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFirewallDomainListsInput:
    out: ListFirewallDomainListsInput = {}  # type: ignore[typeddict-item]
    return out
