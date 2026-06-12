"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteServiceNetworkResourceAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_network_resource_association_identifier


class DeleteServiceNetworkResourceAssociationRequest(TypedDict):
    service_network_resource_association_identifier: "aws_sdk_vpc_lattice.types.service_network_resource_association_identifier.ServiceNetworkResourceAssociationIdentifier"
    """<p>The ID of the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceNetworkResourceAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteServiceNetworkResourceAssociationRequest:
    out: DeleteServiceNetworkResourceAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
