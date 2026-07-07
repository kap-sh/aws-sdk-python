"""Generated from Smithy shape ``com.amazonaws.guardduty#Ec2Vpc``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.ec2_instance_uids


class Ec2Vpc(TypedDict, closed=True):
    ec2_instance_uids: NotRequired[
        "aws_sdk_guardduty.types.ec2_instance_uids.Ec2InstanceUids"
    ]
    """<p>A list of unique identifiers for the compromised Amazon EC2 instances that were launched within the same Virtual Private Cloud (VPC).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2Vpc) -> dict:
    out: dict = {}
    if "ec2_instance_uids" in value:
        import aws_sdk_guardduty.types.ec2_instance_uids

        out["ec2InstanceUids"] = (
            aws_sdk_guardduty.types.ec2_instance_uids.serialize_json(
                value["ec2_instance_uids"]
            )
        )
    return out


def deserialize_json(data: dict) -> Ec2Vpc:
    out: Ec2Vpc = {}  # type: ignore[typeddict-item]
    if "ec2InstanceUids" in data:
        import aws_sdk_guardduty.types.ec2_instance_uids

        out["ec2_instance_uids"] = (
            aws_sdk_guardduty.types.ec2_instance_uids.deserialize_json(
                data["ec2InstanceUids"]
            )
        )
    return out
