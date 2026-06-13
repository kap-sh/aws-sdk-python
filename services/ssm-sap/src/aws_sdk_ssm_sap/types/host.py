"""Generated from Smithy shape ``com.amazonaws.ssmsap#Host``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.host_role


class Host(TypedDict):
    host_name: NotRequired["str"]
    """<p>The name of the Dedicated Host.</p>"""
    host_ip: NotRequired["str"]
    """<p>The IP address of the Dedicated Host. </p>"""
    ec2_instance_id: NotRequired["str"]
    """<p>The ID of Amazon EC2 instance.</p>"""
    instance_id: NotRequired["str"]
    """<p>The instance ID of the instance on the Dedicated Host.</p>"""
    host_role: NotRequired["aws_sdk_ssm_sap.types.host_role.HostRole"]
    """<p>The role of the Dedicated Host.</p>"""
    os_version: NotRequired["str"]
    """<p>The version of the operating system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Host) -> dict:
    out: dict = {}
    if "host_name" in value:
        out["HostName"] = value["host_name"]
    if "host_ip" in value:
        out["HostIp"] = value["host_ip"]
    if "ec2_instance_id" in value:
        out["EC2InstanceId"] = value["ec2_instance_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "host_role" in value:
        import aws_sdk_ssm_sap.types.host_role

        out["HostRole"] = aws_sdk_ssm_sap.types.host_role.serialize_json(
            value["host_role"]
        )
    if "os_version" in value:
        out["OsVersion"] = value["os_version"]
    return out


def deserialize_json(data: dict) -> Host:
    out: Host = {}  # type: ignore[typeddict-item]
    if "HostName" in data:
        out["host_name"] = data["HostName"]
    if "HostIp" in data:
        out["host_ip"] = data["HostIp"]
    if "EC2InstanceId" in data:
        out["ec2_instance_id"] = data["EC2InstanceId"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "HostRole" in data:
        import aws_sdk_ssm_sap.types.host_role

        out["host_role"] = aws_sdk_ssm_sap.types.host_role.deserialize_json(
            data["HostRole"]
        )
    if "OsVersion" in data:
        out["os_version"] = data["OsVersion"]
    return out
