"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListServiceNetworkServiceAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.service_identifier
    import aws_sdk_vpc_lattice.types.service_network_identifier


class ListServiceNetworkServiceAssociationsRequest(TypedDict):
    service_network_identifier: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
    ]
    """<p>The ID or ARN of the service network.</p>"""
    service_identifier: NotRequired[
        "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier"
    ]
    """<p>The ID or ARN of the service.</p>"""
    max_results: NotRequired["aws_sdk_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>A pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceNetworkServiceAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServiceNetworkServiceAssociationsRequest:
    out: ListServiceNetworkServiceAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
