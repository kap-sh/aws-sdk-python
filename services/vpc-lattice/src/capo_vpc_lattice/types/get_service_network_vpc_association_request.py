"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetServiceNetworkVpcAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.service_network_vpc_association_identifier


class GetServiceNetworkVpcAssociationRequest(TypedDict, closed=True):
    service_network_vpc_association_identifier: "capo_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier"
    """<p>The ID or ARN of the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceNetworkVpcAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServiceNetworkVpcAssociationRequest:
    out: GetServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
