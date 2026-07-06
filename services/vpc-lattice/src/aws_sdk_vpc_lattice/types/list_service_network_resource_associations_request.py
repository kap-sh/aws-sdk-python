"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListServiceNetworkResourceAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.resource_configuration_identifier
    import aws_sdk_vpc_lattice.types.service_network_identifier


class ListServiceNetworkResourceAssociationsRequest(TypedDict, closed=True):
    service_network_identifier: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
    ]
    """<p>The ID of the service network.</p>"""
    resource_configuration_identifier: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
    ]
    """<p>The ID of the resource configuration.</p>"""
    max_results: NotRequired["aws_sdk_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum page size.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""
    include_children: NotRequired["bool"]
    """<p>Include service network resource associations of the child resource configuration with the grouped resource configuration.</p> <p>The type is boolean and the default value is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceNetworkResourceAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServiceNetworkResourceAssociationsRequest:
    out: ListServiceNetworkResourceAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
