"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ListScopesInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.max_results

class ListScopesInput(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    max_results: NotRequired["aws_sdk_networkflowmonitor.types.max_results.MaxResults"]
    """<p>The number of query results that you want to return with this call.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListScopesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListScopesInput:
    out: ListScopesInput = {}  # type: ignore[typeddict-item]
    return out