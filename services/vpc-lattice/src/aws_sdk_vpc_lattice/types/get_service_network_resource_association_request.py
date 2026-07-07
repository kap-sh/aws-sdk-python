"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetServiceNetworkResourceAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_network_resource_association_identifier


class GetServiceNetworkResourceAssociationRequest(TypedDict, closed=True):
    service_network_resource_association_identifier: "aws_sdk_vpc_lattice.types.service_network_resource_association_identifier.ServiceNetworkResourceAssociationIdentifier"
    """<p>The ID of the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceNetworkResourceAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServiceNetworkResourceAssociationRequest:
    out: GetServiceNetworkResourceAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
