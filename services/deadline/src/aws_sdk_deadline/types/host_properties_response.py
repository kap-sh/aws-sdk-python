"""Generated from Smithy shape ``com.amazonaws.deadline#HostPropertiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.host_name
    import aws_sdk_deadline.types.instance_type
    import aws_sdk_deadline.types.ip_addresses
    import aws_sdk_deadline.types.string


class HostPropertiesResponse(TypedDict, closed=True):
    ip_addresses: NotRequired["aws_sdk_deadline.types.ip_addresses.IpAddresses"]
    """<p>The IP address of the host.</p>"""
    host_name: NotRequired["aws_sdk_deadline.types.host_name.HostName"]
    """<p>The host name.</p>"""
    ec2_instance_arn: NotRequired["aws_sdk_deadline.types.string.String"]
    """<p>The ARN of the host EC2 instance.</p>"""
    ec2_instance_type: NotRequired["aws_sdk_deadline.types.instance_type.InstanceType"]
    """<p>The instance type of the host EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HostPropertiesResponse) -> dict:
    out: dict = {}
    if "ip_addresses" in value:
        import aws_sdk_deadline.types.ip_addresses

        out["ipAddresses"] = aws_sdk_deadline.types.ip_addresses.serialize_json(
            value["ip_addresses"]
        )
    if "host_name" in value:
        out["hostName"] = value["host_name"]
    if "ec2_instance_arn" in value:
        out["ec2InstanceArn"] = value["ec2_instance_arn"]
    if "ec2_instance_type" in value:
        out["ec2InstanceType"] = value["ec2_instance_type"]
    return out


def deserialize_json(data: dict) -> HostPropertiesResponse:
    out: HostPropertiesResponse = {}  # type: ignore[typeddict-item]
    if "ipAddresses" in data:
        import aws_sdk_deadline.types.ip_addresses

        out["ip_addresses"] = aws_sdk_deadline.types.ip_addresses.deserialize_json(
            data["ipAddresses"]
        )
    if "hostName" in data:
        out["host_name"] = data["hostName"]
    if "ec2InstanceArn" in data:
        out["ec2_instance_arn"] = data["ec2InstanceArn"]
    if "ec2InstanceType" in data:
        out["ec2_instance_type"] = data["ec2InstanceType"]
    return out
