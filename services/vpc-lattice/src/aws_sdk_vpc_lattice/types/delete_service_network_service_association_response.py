"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteServiceNetworkServiceAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_network_service_association_arn
    import aws_sdk_vpc_lattice.types.service_network_service_association_identifier
    import aws_sdk_vpc_lattice.types.service_network_service_association_status


class DeleteServiceNetworkServiceAssociationResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier"
    ]
    """<p>The ID of the association.</p>"""
    status: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_service_association_status.ServiceNetworkServiceAssociationStatus"
    ]
    """<p>The status. You can retry the operation if the status is <code>DELETE_FAILED</code>. However, if you retry it when the status is <code>DELETE_IN_PROGRESS</code>, there is no change in the status.</p>"""
    arn: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_service_association_arn.ServiceNetworkServiceAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceNetworkServiceAssociationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteServiceNetworkServiceAssociationResponse:
    out: DeleteServiceNetworkServiceAssociationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
