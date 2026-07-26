"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListAccessTokensInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.filters
    import capo_route53globalresolver.types.resource_id


class ListAccessTokensInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to retrieve in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response.</p>"""
    dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view to list the tokens for.</p>"""
    filters: NotRequired["capo_route53globalresolver.types.filters.Filters"]
    """<p>Filtering parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessTokensInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccessTokensInput:
    out: ListAccessTokensInput = {}  # type: ignore[typeddict-item]
    return out
