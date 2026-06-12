"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateResourceGatewayResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.ip_address_type
    import aws_sdk_vpc_lattice.types.resource_gateway_arn
    import aws_sdk_vpc_lattice.types.resource_gateway_id
    import aws_sdk_vpc_lattice.types.resource_gateway_name
    import aws_sdk_vpc_lattice.types.resource_gateway_status
    import aws_sdk_vpc_lattice.types.security_group_list
    import aws_sdk_vpc_lattice.types.subnet_list
    import aws_sdk_vpc_lattice.types.vpc_id


class UpdateResourceGatewayResponse(TypedDict):
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
    vpc_id: NotRequired["aws_sdk_vpc_lattice.types.vpc_id.VpcId"]
    """<p>The ID of the VPC for the resource gateway.</p>"""
    subnet_ids: NotRequired["aws_sdk_vpc_lattice.types.subnet_list.SubnetList"]
    """<p>The IDs of the VPC subnets for the resource gateway.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList"
    ]
    """<p>The IDs of the security groups associated with the resource gateway.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_vpc_lattice.types.ip_address_type.IpAddressType"
    ]
    """<p>The type of IP address used by the resource gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceGatewayResponse) -> dict:
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
    if "security_group_ids" in value:
        import aws_sdk_vpc_lattice.types.security_group_list

        out["securityGroupIds"] = (
            aws_sdk_vpc_lattice.types.security_group_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "ip_address_type" in value:
        out["ipAddressType"] = value["ip_address_type"]
    return out


def deserialize_json(data: dict) -> UpdateResourceGatewayResponse:
    out: UpdateResourceGatewayResponse = {}  # type: ignore[typeddict-item]
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
    if "securityGroupIds" in data:
        import aws_sdk_vpc_lattice.types.security_group_list

        out["security_group_ids"] = (
            aws_sdk_vpc_lattice.types.security_group_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "ipAddressType" in data:
        out["ip_address_type"] = data["ipAddressType"]
    return out
