"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListResourceGatewaysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token


class ListResourceGatewaysRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum page size.</p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceGatewaysRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListResourceGatewaysRequest:
    out: ListResourceGatewaysRequest = {}  # type: ignore[typeddict-item]
    return out
