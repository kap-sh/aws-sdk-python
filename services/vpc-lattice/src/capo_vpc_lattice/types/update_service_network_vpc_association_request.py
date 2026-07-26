"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateServiceNetworkVpcAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_vpc_lattice.types.security_group_list
    import capo_vpc_lattice.types.service_network_vpc_association_identifier


class UpdateServiceNetworkVpcAssociationRequest(TypedDict, closed=True):
    service_network_vpc_association_identifier: "capo_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier"
    """<p>The ID or ARN of the association.</p>"""
    security_group_ids: "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
    """<p>The IDs of the security groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceNetworkVpcAssociationRequest) -> dict:
    out: dict = {}
    import capo_vpc_lattice.types.security_group_list

    out["securityGroupIds"] = capo_vpc_lattice.types.security_group_list.serialize_json(
        value["security_group_ids"]
    )
    return out


def deserialize_json(data: dict) -> UpdateServiceNetworkVpcAssociationRequest:
    out: UpdateServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
    if "securityGroupIds" in data:
        import capo_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            capo_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateServiceNetworkVpcAssociationRequest.security_group_ids required"
        )
    return out
