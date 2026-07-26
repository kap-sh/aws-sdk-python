"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteServiceNetworkServiceAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.service_network_service_association_identifier


class DeleteServiceNetworkServiceAssociationRequest(TypedDict, closed=True):
    service_network_service_association_identifier: "capo_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier"
    """<p>The ID or ARN of the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceNetworkServiceAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteServiceNetworkServiceAssociationRequest:
    out: DeleteServiceNetworkServiceAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
