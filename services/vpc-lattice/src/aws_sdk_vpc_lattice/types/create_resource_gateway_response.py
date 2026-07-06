"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateResourceGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.ipv4_addresses_per_eni
    import aws_sdk_vpc_lattice.types.resource_config_dns_resolution
    import aws_sdk_vpc_lattice.types.resource_gateway_arn
    import aws_sdk_vpc_lattice.types.resource_gateway_id
    import aws_sdk_vpc_lattice.types.resource_gateway_ip_address_type
    import aws_sdk_vpc_lattice.types.resource_gateway_name
    import aws_sdk_vpc_lattice.types.resource_gateway_status
    import aws_sdk_vpc_lattice.types.security_group_list
    import aws_sdk_vpc_lattice.types.subnet_list
    import aws_sdk_vpc_lattice.types.vpc_id


class CreateResourceGatewayResponse(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_gateway_name.ResourceGatewayName"
    ]
    """<p>The name of the resource gateway.</p>"""
    id: NotRequired["aws_sdk_vpc_lattice.types.resource_gateway_id.ResourceGatewayId"]
    """<p>The ID of the resource gateway.</p>"""
    arn: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_gateway_arn.ResourceGatewayArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource gateway.</p>"""
    status: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_gateway_status.ResourceGatewayStatus"
    ]
    """<p>The status of the resource gateway.</p>"""
    vpc_identifier: NotRequired["aws_sdk_vpc_lattice.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    subnet_ids: NotRequired["aws_sdk_vpc_lattice.types.subnet_list.SubnetList"]
    """<p>The IDs of the resource gateway subnets.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The IDs of the security groups for the resource gateway.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_gateway_ip_address_type.ResourceGatewayIpAddressType"
    ]
    """<p>The type of IP address for the resource gateway.</p>"""
    ipv4_addresses_per_eni: NotRequired[
        "aws_sdk_vpc_lattice.types.ipv4_addresses_per_eni.Ipv4AddressesPerEni"
    ]
    """<p>The number of IPv4 addresses in each ENI for the resource gateway.</p>"""
    resource_config_dns_resolution: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
    ]
    """<p>The DNS resolution type for resource configurations that are associated with this resource gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourceGatewayResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "vpc_identifier" in value:
        out["vpcIdentifier"] = value["vpc_identifier"]
    if "subnet_ids" in value:
        import aws_sdk_vpc_lattice.types.subnet_list

        out["subnetIds"] = aws_sdk_vpc_lattice.types.subnet_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import aws_sdk_vpc_lattice.types.security_group_list

        out["securityGroupIds"] = (
            aws_sdk_vpc_lattice.types.security_group_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "ip_address_type" in value:
        out["ipAddressType"] = value["ip_address_type"]
    if "ipv4_addresses_per_eni" in value:
        out["ipv4AddressesPerEni"] = value["ipv4_addresses_per_eni"]
    if "resource_config_dns_resolution" in value:
        out["resourceConfigDnsResolution"] = value["resource_config_dns_resolution"]
    return out


def deserialize_json(data: dict) -> CreateResourceGatewayResponse:
    out: CreateResourceGatewayResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        out["status"] = data["status"]
    if "vpcIdentifier" in data:
        out["vpc_identifier"] = data["vpcIdentifier"]
    if "subnetIds" in data:
        import aws_sdk_vpc_lattice.types.subnet_list

        out["subnet_ids"] = aws_sdk_vpc_lattice.types.subnet_list.deserialize_json(
            data["subnetIds"]
        )
    if "securityGroupIds" in data:
        import aws_sdk_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            aws_sdk_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "ipAddressType" in data:
        out["ip_address_type"] = data["ipAddressType"]
    if "ipv4AddressesPerEni" in data:
        out["ipv4_addresses_per_eni"] = data["ipv4AddressesPerEni"]
    if "resourceConfigDnsResolution" in data:
        out["resource_config_dns_resolution"] = data["resourceConfigDnsResolution"]
    return out
