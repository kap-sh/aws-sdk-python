"""Generated from Smithy shape ``com.amazonaws.guardduty#EcsCluster``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.ec2_instance_uids
    import aws_sdk_guardduty.types.ecs_cluster_status


class EcsCluster(TypedDict):
    status: NotRequired["aws_sdk_guardduty.types.ecs_cluster_status.EcsClusterStatus"]
    """<p>The current status of the Amazon ECS cluster.</p>"""
    ec2_instance_uids: NotRequired[
        "aws_sdk_guardduty.types.ec2_instance_uids.Ec2InstanceUids"
    ]
    """<p>A list of unique identifiers for the Amazon EC2 instances that serve as container instances in the Amazon ECS cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsCluster) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_guardduty.types.ecs_cluster_status

        out["status"] = aws_sdk_guardduty.types.ecs_cluster_status.serialize_json(
            value["status"]
        )
    if "ec2_instance_uids" in value:
        import aws_sdk_guardduty.types.ec2_instance_uids

        out["ec2InstanceUids"] = (
            aws_sdk_guardduty.types.ec2_instance_uids.serialize_json(
                value["ec2_instance_uids"]
            )
        )
    return out


def deserialize_json(data: dict) -> EcsCluster:
    out: EcsCluster = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_guardduty.types.ecs_cluster_status

        out["status"] = aws_sdk_guardduty.types.ecs_cluster_status.deserialize_json(
            data["status"]
        )
    if "ec2InstanceUids" in data:
        import aws_sdk_guardduty.types.ec2_instance_uids

        out["ec2_instance_uids"] = (
            aws_sdk_guardduty.types.ec2_instance_uids.deserialize_json(
                data["ec2InstanceUids"]
            )
        )
    return out
