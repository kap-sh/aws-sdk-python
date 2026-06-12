"""Generated from Smithy shape ``com.amazonaws.s3outposts#Endpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3outposts.types.cidr_block
    import aws_sdk_s3outposts.types.creation_time
    import aws_sdk_s3outposts.types.customer_owned_ipv4_pool
    import aws_sdk_s3outposts.types.endpoint_access_type
    import aws_sdk_s3outposts.types.endpoint_arn
    import aws_sdk_s3outposts.types.endpoint_status
    import aws_sdk_s3outposts.types.failed_reason
    import aws_sdk_s3outposts.types.network_interfaces
    import aws_sdk_s3outposts.types.outpost_id
    import aws_sdk_s3outposts.types.security_group_id
    import aws_sdk_s3outposts.types.subnet_id
    import aws_sdk_s3outposts.types.vpc_id


class Endpoint(TypedDict):
    endpoint_arn: NotRequired["aws_sdk_s3outposts.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""
    outposts_id: NotRequired["aws_sdk_s3outposts.types.outpost_id.OutpostId"]
    """<p>The ID of the Outposts.</p>"""
    cidr_block: NotRequired["aws_sdk_s3outposts.types.cidr_block.CidrBlock"]
    """<p>The VPC CIDR committed by this endpoint.</p>"""
    status: NotRequired["aws_sdk_s3outposts.types.endpoint_status.EndpointStatus"]
    """<p>The status of the endpoint.</p>"""
    creation_time: NotRequired["aws_sdk_s3outposts.types.creation_time.CreationTime"]
    """<p>The time the endpoint was created.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_s3outposts.types.network_interfaces.NetworkInterfaces"
    ]
    """<p>The network interface of the endpoint.</p>"""
    vpc_id: NotRequired["aws_sdk_s3outposts.types.vpc_id.VpcId"]
    """<p>The ID of the VPC used for the endpoint.</p>"""
    subnet_id: NotRequired["aws_sdk_s3outposts.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet used for the endpoint.</p>"""
    security_group_id: NotRequired[
        "aws_sdk_s3outposts.types.security_group_id.SecurityGroupId"
    ]
    """<p>The ID of the security group used for the endpoint.</p>"""
    access_type: NotRequired[
        "aws_sdk_s3outposts.types.endpoint_access_type.EndpointAccessType"
    ]
    """<p>The type of connectivity used to access the Amazon S3 on Outposts endpoint.</p>"""
    customer_owned_ipv4_pool: NotRequired[
        "aws_sdk_s3outposts.types.customer_owned_ipv4_pool.CustomerOwnedIpv4Pool"
    ]
    """<p>The ID of the customer-owned IPv4 address pool used for the endpoint.</p>"""
    failed_reason: NotRequired["aws_sdk_s3outposts.types.failed_reason.FailedReason"]
    """<p>The failure reason, if any, for a create or delete endpoint operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Endpoint) -> dict:
    out: dict = {}
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "outposts_id" in value:
        out["OutpostsId"] = value["outposts_id"]
    if "cidr_block" in value:
        out["CidrBlock"] = value["cidr_block"]
    if "status" in value:
        import aws_sdk_s3outposts.types.endpoint_status

        out["Status"] = aws_sdk_s3outposts.types.endpoint_status.serialize_json(
            value["status"]
        )
    if "creation_time" in value:
        import aws_sdk_s3outposts.types.creation_time

        out["CreationTime"] = aws_sdk_s3outposts.types.creation_time.serialize_json(
            value["creation_time"]
        )
    if "network_interfaces" in value:
        import aws_sdk_s3outposts.types.network_interfaces

        out["NetworkInterfaces"] = (
            aws_sdk_s3outposts.types.network_interfaces.serialize_json(
                value["network_interfaces"]
            )
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "security_group_id" in value:
        out["SecurityGroupId"] = value["security_group_id"]
    if "access_type" in value:
        import aws_sdk_s3outposts.types.endpoint_access_type

        out["AccessType"] = (
            aws_sdk_s3outposts.types.endpoint_access_type.serialize_json(
                value["access_type"]
            )
        )
    if "customer_owned_ipv4_pool" in value:
        out["CustomerOwnedIpv4Pool"] = value["customer_owned_ipv4_pool"]
    if "failed_reason" in value:
        import aws_sdk_s3outposts.types.failed_reason

        out["FailedReason"] = aws_sdk_s3outposts.types.failed_reason.serialize_json(
            value["failed_reason"]
        )
    return out


def deserialize_json(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    if "OutpostsId" in data:
        out["outposts_id"] = data["OutpostsId"]
    if "CidrBlock" in data:
        out["cidr_block"] = data["CidrBlock"]
    if "Status" in data:
        import aws_sdk_s3outposts.types.endpoint_status

        out["status"] = aws_sdk_s3outposts.types.endpoint_status.deserialize_json(
            data["Status"]
        )
    if "CreationTime" in data:
        import aws_sdk_s3outposts.types.creation_time

        out["creation_time"] = aws_sdk_s3outposts.types.creation_time.deserialize_json(
            data["CreationTime"]
        )
    if "NetworkInterfaces" in data:
        import aws_sdk_s3outposts.types.network_interfaces

        out["network_interfaces"] = (
            aws_sdk_s3outposts.types.network_interfaces.deserialize_json(
                data["NetworkInterfaces"]
            )
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "SecurityGroupId" in data:
        out["security_group_id"] = data["SecurityGroupId"]
    if "AccessType" in data:
        import aws_sdk_s3outposts.types.endpoint_access_type

        out["access_type"] = (
            aws_sdk_s3outposts.types.endpoint_access_type.deserialize_json(
                data["AccessType"]
            )
        )
    if "CustomerOwnedIpv4Pool" in data:
        out["customer_owned_ipv4_pool"] = data["CustomerOwnedIpv4Pool"]
    if "FailedReason" in data:
        import aws_sdk_s3outposts.types.failed_reason

        out["failed_reason"] = aws_sdk_s3outposts.types.failed_reason.deserialize_json(
            data["FailedReason"]
        )
    return out
