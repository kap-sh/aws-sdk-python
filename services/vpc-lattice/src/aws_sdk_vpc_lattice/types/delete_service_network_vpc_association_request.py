"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteServiceNetworkVpcAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_identifier


class DeleteServiceNetworkVpcAssociationRequest(TypedDict):
    service_network_vpc_association_identifier: "aws_sdk_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier"
    """<p>The ID or ARN of the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceNetworkVpcAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteServiceNetworkVpcAssociationRequest:
    out: DeleteServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
