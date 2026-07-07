"""Generated from Smithy shape ``com.amazonaws.guardduty#EksCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.cluster_status
    import aws_sdk_guardduty.types.ec2_instance_uids
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.timestamp


class EksCluster(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the Amazon EKS cluster involved in the finding.</p>"""
    created_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp indicating when the Amazon EKS cluster was created, in UTC format.</p>"""
    status: NotRequired["aws_sdk_guardduty.types.cluster_status.ClusterStatus"]
    """<p>The current status of the Amazon EKS cluster.</p>"""
    vpc_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ID of the Amazon Virtual Private Cloud (Amazon VPC) associated with the Amazon EKS cluster.</p>"""
    ec2_instance_uids: NotRequired[
        "aws_sdk_guardduty.types.ec2_instance_uids.Ec2InstanceUids"
    ]
    """<p>A list of unique identifiers for the Amazon EC2 instances that serve as worker nodes in the Amazon EKS cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksCluster) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["createdAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "status" in value:
        import aws_sdk_guardduty.types.cluster_status

        out["status"] = aws_sdk_guardduty.types.cluster_status.serialize_json(
            value["status"]
        )
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "ec2_instance_uids" in value:
        import aws_sdk_guardduty.types.ec2_instance_uids

        out["ec2InstanceUids"] = (
            aws_sdk_guardduty.types.ec2_instance_uids.serialize_json(
                value["ec2_instance_uids"]
            )
        )
    return out


def deserialize_json(data: dict) -> EksCluster:
    out: EksCluster = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["created_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "status" in data:
        import aws_sdk_guardduty.types.cluster_status

        out["status"] = aws_sdk_guardduty.types.cluster_status.deserialize_json(
            data["status"]
        )
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "ec2InstanceUids" in data:
        import aws_sdk_guardduty.types.ec2_instance_uids

        out["ec2_instance_uids"] = (
            aws_sdk_guardduty.types.ec2_instance_uids.deserialize_json(
                data["ec2InstanceUids"]
            )
        )
    return out
