"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListDNSViewsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.resource_id


class ListDNSViewsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to retrieve in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response.</p>"""
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The Global Resolver ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDNSViewsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDNSViewsInput:
    out: ListDNSViewsInput = {}  # type: ignore[typeddict-item]
    return out
