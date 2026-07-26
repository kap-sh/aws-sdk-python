"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListAccessLogSubscriptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.resource_identifier


class ListAccessLogSubscriptionsRequest(TypedDict, closed=True):
    resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier"
    """<p>The ID or ARN of the service network or service.</p>"""
    max_results: NotRequired["capo_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p>A pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessLogSubscriptionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccessLogSubscriptionsRequest:
    out: ListAccessLogSubscriptionsRequest = {}  # type: ignore[typeddict-item]
    return out
