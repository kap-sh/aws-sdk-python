"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateServiceNetworkVpcAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.account_id
    import capo_vpc_lattice.types.security_group_list
    import capo_vpc_lattice.types.service_network_vpc_association_arn
    import capo_vpc_lattice.types.service_network_vpc_association_id
    import capo_vpc_lattice.types.service_network_vpc_association_status


class UpdateServiceNetworkVpcAssociationResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_vpc_lattice.types.service_network_vpc_association_id.ServiceNetworkVpcAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    arn: NotRequired[
        "capo_vpc_lattice.types.service_network_vpc_association_arn.ServiceNetworkVpcAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    status: NotRequired[
        "capo_vpc_lattice.types.service_network_vpc_association_status.ServiceNetworkVpcAssociationStatus"
    ]
    """<p>The status. You can retry the operation if the status is <code>DELETE_FAILED</code>. However, if you retry it while the status is <code>DELETE_IN_PROGRESS</code>, there is no change in the status.</p>"""
    created_by: NotRequired["capo_vpc_lattice.types.account_id.AccountId"]
    """<p>The account that created the association.</p>"""
    security_group_ids: NotRequired[
        "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The IDs of the security groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceNetworkVpcAssociationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "security_group_ids" in value:
        import capo_vpc_lattice.types.security_group_list

        out["securityGroupIds"] = (
            capo_vpc_lattice.types.security_group_list.serialize_json(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateServiceNetworkVpcAssociationResponse:
    out: UpdateServiceNetworkVpcAssociationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        out["status"] = data["status"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "securityGroupIds" in data:
        import capo_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            capo_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    return out
