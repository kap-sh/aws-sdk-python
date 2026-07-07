"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteServiceNetworkResourceAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_network_resource_association_arn
    import aws_sdk_vpc_lattice.types.service_network_resource_association_id
    import aws_sdk_vpc_lattice.types.service_network_resource_association_status


class DeleteServiceNetworkResourceAssociationResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_resource_association_id.ServiceNetworkResourceAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    arn: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_resource_association_arn.ServiceNetworkResourceAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    status: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_resource_association_status.ServiceNetworkResourceAssociationStatus"
    ]
    """<p>The status of the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceNetworkResourceAssociationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DeleteServiceNetworkResourceAssociationResponse:
    out: DeleteServiceNetworkResourceAssociationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        out["status"] = data["status"]
    return out
