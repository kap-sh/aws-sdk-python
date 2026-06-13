"""Generated from Smithy shape ``com.amazonaws.emr#ClusterSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.arn_type
    import aws_sdk_emr.types.cluster_id
    import aws_sdk_emr.types.cluster_status
    import aws_sdk_emr.types.integer
    import aws_sdk_emr.types.optional_arn_type
    import aws_sdk_emr.types.string


class ClusterSummary(TypedDict):
    id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p>The unique identifier for the cluster.</p>"""
    name: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The name of the cluster.</p>"""
    status: NotRequired["aws_sdk_emr.types.cluster_status.ClusterStatus"]
    """<p>The details about the current status of the cluster.</p>"""
    normalized_instance_hours: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>An approximation of the cost of the cluster, represented in m1.small/hours. This value is incremented one time for every hour an m1.small instance runs. Larger instances are weighted more, so an Amazon EC2 instance that is roughly four times more expensive would result in the normalized instance hours being incremented by four. This result is only an approximation and does not reflect the actual billing rate.</p>"""
    cluster_arn: NotRequired["aws_sdk_emr.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name of the cluster.</p>"""
    outpost_arn: NotRequired["aws_sdk_emr.types.optional_arn_type.OptionalArnType"]
    """<p> The Amazon Resource Name (ARN) of the Outpost where the cluster is launched. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_emr.types.cluster_status

        out["Status"] = aws_sdk_emr.types.cluster_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "normalized_instance_hours" in value:
        out["NormalizedInstanceHours"] = value["normalized_instance_hours"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterSummary:
    out: ClusterSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_emr.types.cluster_status

        out["status"] = aws_sdk_emr.types.cluster_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "NormalizedInstanceHours" in data:
        out["normalized_instance_hours"] = data["NormalizedInstanceHours"]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "OutpostArn" in data:
        out["outpost_arn"] = data["OutpostArn"]
    return out
