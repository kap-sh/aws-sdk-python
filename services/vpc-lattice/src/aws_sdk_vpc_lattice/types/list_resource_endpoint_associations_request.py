"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListResourceEndpointAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.resource_configuration_identifier
    import aws_sdk_vpc_lattice.types.resource_endpoint_association_identifier
    import aws_sdk_vpc_lattice.types.vpc_endpoint_id
    import aws_sdk_vpc_lattice.types.vpc_endpoint_owner


class ListResourceEndpointAssociationsRequest(TypedDict, closed=True):
    resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
    """<p>The ID for the resource configuration associated with the VPC endpoint.</p>"""
    resource_endpoint_association_identifier: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier"
    ]
    """<p>The ID of the association.</p>"""
    vpc_endpoint_id: NotRequired[
        "aws_sdk_vpc_lattice.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>The ID of the VPC endpoint in the association.</p>"""
    vpc_endpoint_owner: NotRequired[
        "aws_sdk_vpc_lattice.types.vpc_endpoint_owner.VpcEndpointOwner"
    ]
    """<p>The owner of the VPC endpoint in the association.</p>"""
    max_results: NotRequired["aws_sdk_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum page size.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>A pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceEndpointAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListResourceEndpointAssociationsRequest:
    out: ListResourceEndpointAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
