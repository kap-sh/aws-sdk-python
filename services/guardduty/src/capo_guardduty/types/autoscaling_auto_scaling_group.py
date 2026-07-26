"""Generated from Smithy shape ``com.amazonaws.guardduty#AutoscalingAutoScalingGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.ec2_instance_uids


class AutoscalingAutoScalingGroup(TypedDict, closed=True):
    ec2_instance_uids: NotRequired[
        "capo_guardduty.types.ec2_instance_uids.Ec2InstanceUids"
    ]
    """<p>A list of unique identifiers for the compromised Amazon EC2 instances that are part of the same Auto Scaling Group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoscalingAutoScalingGroup) -> dict:
    out: dict = {}
    if "ec2_instance_uids" in value:
        import capo_guardduty.types.ec2_instance_uids

        out["ec2InstanceUids"] = capo_guardduty.types.ec2_instance_uids.serialize_json(
            value["ec2_instance_uids"]
        )
    return out


def deserialize_json(data: dict) -> AutoscalingAutoScalingGroup:
    out: AutoscalingAutoScalingGroup = {}  # type: ignore[typeddict-item]
    if "ec2InstanceUids" in data:
        import capo_guardduty.types.ec2_instance_uids

        out["ec2_instance_uids"] = (
            capo_guardduty.types.ec2_instance_uids.deserialize_json(
                data["ec2InstanceUids"]
            )
        )
    return out
