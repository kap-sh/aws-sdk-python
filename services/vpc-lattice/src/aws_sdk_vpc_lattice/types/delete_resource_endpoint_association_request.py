"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteResourceEndpointAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.resource_endpoint_association_identifier


class DeleteResourceEndpointAssociationRequest(TypedDict, closed=True):
    resource_endpoint_association_identifier: "aws_sdk_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier"
    """<p>The ID or ARN of the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceEndpointAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourceEndpointAssociationRequest:
    out: DeleteResourceEndpointAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
