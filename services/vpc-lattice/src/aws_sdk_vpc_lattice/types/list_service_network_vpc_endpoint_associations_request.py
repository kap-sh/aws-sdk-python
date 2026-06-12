"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListServiceNetworkVpcEndpointAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.service_network_identifier


class ListServiceNetworkVpcEndpointAssociationsRequest(TypedDict):
    service_network_identifier: (
        "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
    )
    """<p>The ID of the service network associated with the VPC endpoint.</p>"""
    max_results: NotRequired["aws_sdk_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum page size.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceNetworkVpcEndpointAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServiceNetworkVpcEndpointAssociationsRequest:
    out: ListServiceNetworkVpcEndpointAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
