"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListFirewallRulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.filters
    import aws_sdk_route53globalresolver.types.resource_id


class ListFirewallRulesInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to retrieve in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response.</p>"""
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the DNS view.</p>"""
    filters: NotRequired["aws_sdk_route53globalresolver.types.filters.Filters"]
    """<p>Values to filter the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFirewallRulesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFirewallRulesInput:
    out: ListFirewallRulesInput = {}  # type: ignore[typeddict-item]
    return out
