"""Generated from Smithy shape ``com.amazonaws.guardduty#EksClusterDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.tags
    import aws_sdk_guardduty.types.timestamp


class EksClusterDetails(TypedDict, closed=True):
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>EKS cluster name.</p>"""
    arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>EKS cluster ARN.</p>"""
    vpc_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The VPC ID to which the EKS cluster is attached.</p>"""
    status: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The EKS cluster status.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tags.Tags"]
    """<p>The EKS cluster tags.</p>"""
    created_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the EKS cluster was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksClusterDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "tags" in value:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.serialize_json(value["tags"])
    if "created_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["createdAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> EksClusterDetails:
    out: EksClusterDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "status" in data:
        out["status"] = data["status"]
    if "tags" in data:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.deserialize_json(data["tags"])
    if "createdAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["created_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    return out
