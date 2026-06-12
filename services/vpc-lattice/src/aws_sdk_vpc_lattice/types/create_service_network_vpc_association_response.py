"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceNetworkVpcAssociationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.account_id
    import aws_sdk_vpc_lattice.types.boolean
    import aws_sdk_vpc_lattice.types.dns_options
    import aws_sdk_vpc_lattice.types.security_group_list
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_arn
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_id
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_status


class CreateServiceNetworkVpcAssociationResponse(TypedDict):
    id: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_vpc_association_id.ServiceNetworkVpcAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    status: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_vpc_association_status.ServiceNetworkVpcAssociationStatus"
    ]
    """<p>The association status.</p>"""
    arn: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_vpc_association_arn.ServiceNetworkVpcAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    created_by: NotRequired["aws_sdk_vpc_lattice.types.account_id.AccountId"]
    """<p>The account that created the association.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The IDs of the security groups.</p>"""
    private_dns_enabled: NotRequired["aws_sdk_vpc_lattice.types.boolean.Boolean"]
    """<p> Indicates if private DNS is enabled for the VPC association. </p>"""
    dns_options: NotRequired["aws_sdk_vpc_lattice.types.dns_options.DnsOptions"]


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
        import aws_sdk_vpc_lattice.types.security_group_list

        out["securityGroupIds"] = (
            aws_sdk_vpc_lattice.types.security_group_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "private_dns_enabled" in value:
        out["privateDnsEnabled"] = value["private_dns_enabled"]
    if "dns_options" in value:
        import aws_sdk_vpc_lattice.types.dns_options

        out["dnsOptions"] = aws_sdk_vpc_lattice.types.dns_options.serialize_json(
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
        import aws_sdk_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            aws_sdk_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "privateDnsEnabled" in data:
        out["private_dns_enabled"] = data["privateDnsEnabled"]
    if "dnsOptions" in data:
        import aws_sdk_vpc_lattice.types.dns_options

        out["dns_options"] = aws_sdk_vpc_lattice.types.dns_options.deserialize_json(
            data["dnsOptions"]
        )
    return out
