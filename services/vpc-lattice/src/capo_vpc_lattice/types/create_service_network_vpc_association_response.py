"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceNetworkVpcAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.account_id
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.dns_options
    import capo_vpc_lattice.types.security_group_list
    import capo_vpc_lattice.types.service_network_vpc_association_arn
    import capo_vpc_lattice.types.service_network_vpc_association_id
    import capo_vpc_lattice.types.service_network_vpc_association_status


class CreateServiceNetworkVpcAssociationResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_vpc_lattice.types.service_network_vpc_association_id.ServiceNetworkVpcAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    status: NotRequired[
        "capo_vpc_lattice.types.service_network_vpc_association_status.ServiceNetworkVpcAssociationStatus"
    ]
    """<p>The association status.</p>"""
    arn: NotRequired[
        "capo_vpc_lattice.types.service_network_vpc_association_arn.ServiceNetworkVpcAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    created_by: NotRequired["capo_vpc_lattice.types.account_id.AccountId"]
    """<p>The account that created the association.</p>"""
    security_group_ids: NotRequired[
        "capo_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The IDs of the security groups.</p>"""
    private_dns_enabled: NotRequired["capo_vpc_lattice.types.boolean.Boolean"]
    """<p> Indicates if private DNS is enabled for the VPC association. </p>"""
    dns_options: NotRequired["capo_vpc_lattice.types.dns_options.DnsOptions"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceNetworkVpcAssociationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "security_group_ids" in value:
        import capo_vpc_lattice.types.security_group_list

        out["securityGroupIds"] = (
            capo_vpc_lattice.types.security_group_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "private_dns_enabled" in value:
        out["privateDnsEnabled"] = value["private_dns_enabled"]
    if "dns_options" in value:
        import capo_vpc_lattice.types.dns_options

        out["dnsOptions"] = capo_vpc_lattice.types.dns_options.serialize_json(
            value["dns_options"]
        )
    return out


def deserialize_json(data: dict) -> CreateServiceNetworkVpcAssociationResponse:
    out: CreateServiceNetworkVpcAssociationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "securityGroupIds" in data:
        import capo_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            capo_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "privateDnsEnabled" in data:
        out["private_dns_enabled"] = data["privateDnsEnabled"]
    if "dnsOptions" in data:
        import capo_vpc_lattice.types.dns_options

        out["dns_options"] = capo_vpc_lattice.types.dns_options.deserialize_json(
            data["dnsOptions"]
        )
    return out
