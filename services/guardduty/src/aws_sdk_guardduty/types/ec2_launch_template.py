"""Generated from Smithy shape ``com.amazonaws.guardduty#Ec2LaunchTemplate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.ec2_instance_uids
    import aws_sdk_guardduty.types.launch_template_version


class Ec2LaunchTemplate(TypedDict):
    ec2_instance_uids: NotRequired[
        "aws_sdk_guardduty.types.ec2_instance_uids.Ec2InstanceUids"
    ]
    """<p>A list of unique identifiers for the compromised Amazon EC2 instances that share the same Amazon EC2 launch template.</p>"""
    version: NotRequired[
        "aws_sdk_guardduty.types.launch_template_version.LaunchTemplateVersion"
    ]
    """<p>Version of the EC2 launch template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2LaunchTemplate) -> dict:
    out: dict = {}
    if "ec2_instance_uids" in value:
        import aws_sdk_guardduty.types.ec2_instance_uids

        out["ec2InstanceUids"] = (
            aws_sdk_guardduty.types.ec2_instance_uids.serialize_json(
                value["ec2_instance_uids"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> Ec2LaunchTemplate:
    out: Ec2LaunchTemplate = {}  # type: ignore[typeddict-item]
    if "ec2InstanceUids" in data:
        import aws_sdk_guardduty.types.ec2_instance_uids

        out["ec2_instance_uids"] = (
            aws_sdk_guardduty.types.ec2_instance_uids.deserialize_json(
                data["ec2InstanceUids"]
            )
        )
    if "version" in data:
        out["version"] = data["version"]
    return out
