"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceNetworkResourceAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.account_id
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.service_network_resource_association_arn
    import capo_vpc_lattice.types.service_network_resource_association_id
    import capo_vpc_lattice.types.service_network_resource_association_status


class CreateServiceNetworkResourceAssociationResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_vpc_lattice.types.service_network_resource_association_id.ServiceNetworkResourceAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    arn: NotRequired[
        "capo_vpc_lattice.types.service_network_resource_association_arn.ServiceNetworkResourceAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    status: NotRequired[
        "capo_vpc_lattice.types.service_network_resource_association_status.ServiceNetworkResourceAssociationStatus"
    ]
    """<p>The status of the association.</p>"""
    created_by: NotRequired["capo_vpc_lattice.types.account_id.AccountId"]
    """<p>The ID of the account that created the association.</p>"""
    private_dns_enabled: NotRequired["capo_vpc_lattice.types.boolean.Boolean"]
    """<p> Indicates if private DNS is is enabled for the service network resource association. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceNetworkResourceAssociationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "private_dns_enabled" in value:
        out["privateDnsEnabled"] = value["private_dns_enabled"]
    return out


def deserialize_json(data: dict) -> CreateServiceNetworkResourceAssociationResponse:
    out: CreateServiceNetworkResourceAssociationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        out["status"] = data["status"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "privateDnsEnabled" in data:
        out["private_dns_enabled"] = data["privateDnsEnabled"]
    return out
