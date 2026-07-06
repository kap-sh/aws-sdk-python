"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListServiceNetworkVpcAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.service_network_identifier
    import aws_sdk_vpc_lattice.types.vpc_id


class ListServiceNetworkVpcAssociationsRequest(TypedDict, closed=True):
    service_network_identifier: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
    ]
    """<p>The ID or ARN of the service network.</p>"""
    vpc_identifier: NotRequired["aws_sdk_vpc_lattice.types.vpc_id.VpcId"]
    """<p>The ID or ARN of the VPC.</p>"""
    max_results: NotRequired["aws_sdk_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>A pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceNetworkVpcAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServiceNetworkVpcAssociationsRequest:
    out: ListServiceNetworkVpcAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
