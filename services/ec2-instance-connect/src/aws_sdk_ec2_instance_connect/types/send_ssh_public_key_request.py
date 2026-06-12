"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#SendSSHPublicKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2_instance_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ec2_instance_connect.types.availability_zone
    import aws_sdk_ec2_instance_connect.types.instance_id
    import aws_sdk_ec2_instance_connect.types.instance_os_user
    import aws_sdk_ec2_instance_connect.types.ssh_public_key


class SendSSHPublicKeyRequest(TypedDict):
    instance_id: "aws_sdk_ec2_instance_connect.types.instance_id.InstanceId"
    """<p>The ID of the EC2 instance.</p>"""
    instance_os_user: (
        "aws_sdk_ec2_instance_connect.types.instance_os_user.InstanceOSUser"
    )
    """<p>The OS user on the EC2 instance for whom the key can be used to authenticate.</p>"""
    ssh_public_key: "aws_sdk_ec2_instance_connect.types.ssh_public_key.SSHPublicKey"
    """<p>The public key material. To use the public key, you must have the matching private key.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_ec2_instance_connect.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone in which the EC2 instance was launched.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendSSHPublicKeyRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["InstanceOSUser"] = value["instance_os_user"]
    out["SSHPublicKey"] = value["ssh_public_key"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SendSSHPublicKeyRequest:
    out: SendSSHPublicKeyRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("SendSSHPublicKeyRequest.instance_id required")
    if "InstanceOSUser" in data:
        out["instance_os_user"] = data["InstanceOSUser"]
    else:
        raise DeserializationError("SendSSHPublicKeyRequest.instance_os_user required")
    if "SSHPublicKey" in data:
        out["ssh_public_key"] = data["SSHPublicKey"]
    else:
        raise DeserializationError("SendSSHPublicKeyRequest.ssh_public_key required")
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    return out
