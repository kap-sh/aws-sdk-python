"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetResourceGatewayResponse``."""

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
    import aws_sdk_vpc_lattice.types.timestamp
    import aws_sdk_vpc_lattice.types.vpc_id


class GetResourceGatewayResponse(TypedDict, closed=True):
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
    """<p>The status for the resource gateway.</p>"""
    vpc_id: NotRequired["aws_sdk_vpc_lattice.types.vpc_id.VpcId"]
    """<p>The ID of the VPC for the resource gateway.</p>"""
    subnet_ids: NotRequired["aws_sdk_vpc_lattice.types.subnet_list.SubnetList"]
    """<p>The IDs of the VPC subnets for resource gateway.</p>"""
    service_managed: NotRequired["bool"]
    """<p>Indicates whether the resource gateway is managed by an AWS service.</p>"""
    managed_by: NotRequired["str"]
    """<p>The AWS service that manages the resource gateway.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The security group IDs associated with the resource gateway.</p>"""
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
    created_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the resource gateway was created, in ISO-8601 format.</p>"""
    last_updated_at: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the resource gateway was last updated, in ISO-8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceGatewayResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import aws_sdk_vpc_lattice.types.subnet_list

        out["subnetIds"] = aws_sdk_vpc_lattice.types.subnet_list.serialize_json(
            value["subnet_ids"]
        )
    if "service_managed" in value:
        out["serviceManaged"] = value["service_managed"]
    if "managed_by" in value:
        out["managedBy"] = value["managed_by"]
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
    if "created_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["createdAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetResourceGatewayResponse:
    out: GetResourceGatewayResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        out["status"] = data["status"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "subnetIds" in data:
        import aws_sdk_vpc_lattice.types.subnet_list

        out["subnet_ids"] = aws_sdk_vpc_lattice.types.subnet_list.deserialize_json(
            data["subnetIds"]
        )
    if "serviceManaged" in data:
        out["service_managed"] = data["serviceManaged"]
    if "managedBy" in data:
        out["managed_by"] = data["managedBy"]
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
    if "createdAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["created_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["last_updated_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
