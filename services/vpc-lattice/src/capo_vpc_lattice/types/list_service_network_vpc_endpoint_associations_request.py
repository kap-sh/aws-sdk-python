"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListServiceNetworkVpcEndpointAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.service_network_identifier


class ListServiceNetworkVpcEndpointAssociationsRequest(TypedDict, closed=True):
    service_network_identifier: (
        "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
    )
    """<p>The ID of the service network associated with the VPC endpoint.</p>"""
    max_results: NotRequired["capo_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum page size.</p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceNetworkVpcEndpointAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServiceNetworkVpcEndpointAssociationsRequest:
    out: ListServiceNetworkVpcEndpointAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
