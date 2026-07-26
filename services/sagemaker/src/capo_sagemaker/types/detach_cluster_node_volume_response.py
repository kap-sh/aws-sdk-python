"""Generated from Smithy shape ``com.amazonaws.sagemaker#DetachClusterNodeVolumeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.cluster_node_id
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.volume_attachment_status
    import capo_sagemaker.types.volume_device_name
    import capo_sagemaker.types.volume_id


class DetachClusterNodeVolumeResponse(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p> The Amazon Resource Name (ARN) of your SageMaker HyperPod cluster where the volume detachment operation was performed. </p>"""
    node_id: NotRequired["capo_sagemaker.types.cluster_node_id.ClusterNodeId"]
    """<p> The unique identifier of the cluster node from which your volume was detached. </p>"""
    volume_id: NotRequired["capo_sagemaker.types.volume_id.VolumeId"]
    """<p> The unique identifier of your EBS volume that was detached. </p>"""
    attach_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p> The original timestamp when your volume was initially attached to the node. </p>"""
    status: NotRequired[
        "capo_sagemaker.types.volume_attachment_status.VolumeAttachmentStatus"
    ]
    """<p> The current status of your volume detachment operation. </p>"""
    device_name: NotRequired["capo_sagemaker.types.volume_device_name.VolumeDeviceName"]
    """<p> The device name assigned to your attached volume on the target instance. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetachClusterNodeVolumeResponse) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "attach_time" in value:
        import capo_sagemaker.types.timestamp

        out["AttachTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["attach_time"]
        )
    if "status" in value:
        import capo_sagemaker.types.volume_attachment_status

        out["Status"] = (
            capo_sagemaker.types.volume_attachment_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetachClusterNodeVolumeResponse:
    out: DetachClusterNodeVolumeResponse = {}  # type: ignore[typeddict-item]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    if "AttachTime" in data:
        import capo_sagemaker.types.timestamp

        out["attach_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["AttachTime"]
        )
    if "Status" in data:
        import capo_sagemaker.types.volume_attachment_status

        out["status"] = (
            capo_sagemaker.types.volume_attachment_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    return out
