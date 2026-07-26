"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ListScopesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.max_results


class ListScopesInput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    max_results: NotRequired["capo_networkflowmonitor.types.max_results.MaxResults"]
    """<p>The number of query results that you want to return with this call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScopesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListScopesInput:
    out: ListScopesInput = {}  # type: ignore[typeddict-item]
    return out
