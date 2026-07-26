"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.listener_identifier
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.service_identifier


class ListRulesRequest(TypedDict, closed=True):
    service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier"
    """<p>The ID or ARN of the listener.</p>"""
    max_results: NotRequired["capo_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p>A pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRulesRequest:
    out: ListRulesRequest = {}  # type: ignore[typeddict-item]
    return out
