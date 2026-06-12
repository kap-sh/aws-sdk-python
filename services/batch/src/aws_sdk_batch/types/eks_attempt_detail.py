"""Generated from Smithy shape ``com.amazonaws.batch#EksAttemptDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.eks_attempt_container_details
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.string


class EksAttemptDetail(TypedDict):
    containers: NotRequired[
        "aws_sdk_batch.types.eks_attempt_container_details.EksAttemptContainerDetails"
    ]
    """<p>The details for the final status of the containers for this job attempt.</p>"""
    init_containers: NotRequired[
        "aws_sdk_batch.types.eks_attempt_container_details.EksAttemptContainerDetails"
    ]
    """<p>The details for the init containers.</p>"""
    eks_cluster_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon EKS cluster.</p>"""
    pod_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the pod for this job attempt.</p>"""
    pod_namespace: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The namespace of the Amazon EKS cluster that the pod exists in.</p>"""
    node_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the node for this job attempt.</p>"""
    started_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the attempt was started (when the attempt transitioned from the <code>STARTING</code> state to the <code>RUNNING</code> state).</p>"""
    stopped_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the attempt was stopped. This happens when the attempt transitioned from the <code>RUNNING</code> state to a terminal state, such as <code>SUCCEEDED</code> or <code>FAILED</code>.</p>"""
    status_reason: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>A short, human-readable string to provide additional details for the current status of the job attempt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksAttemptDetail) -> dict:
    out: dict = {}
    if "containers" in value:
        import aws_sdk_batch.types.eks_attempt_container_details

        out["containers"] = (
            aws_sdk_batch.types.eks_attempt_container_details.serialize_json(
                value["containers"]
            )
        )
    if "init_containers" in value:
        import aws_sdk_batch.types.eks_attempt_container_details

        out["initContainers"] = (
            aws_sdk_batch.types.eks_attempt_container_details.serialize_json(
                value["init_containers"]
            )
        )
    if "eks_cluster_arn" in value:
        out["eksClusterArn"] = value["eks_cluster_arn"]
    if "pod_name" in value:
        out["podName"] = value["pod_name"]
    if "pod_namespace" in value:
        out["podNamespace"] = value["pod_namespace"]
    if "node_name" in value:
        out["nodeName"] = value["node_name"]
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    if "stopped_at" in value:
        out["stoppedAt"] = value["stopped_at"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> EksAttemptDetail:
    out: EksAttemptDetail = {}  # type: ignore[typeddict-item]
    if "containers" in data:
        import aws_sdk_batch.types.eks_attempt_container_details

        out["containers"] = (
            aws_sdk_batch.types.eks_attempt_container_details.deserialize_json(
                data["containers"]
            )
        )
    if "initContainers" in data:
        import aws_sdk_batch.types.eks_attempt_container_details

        out["init_containers"] = (
            aws_sdk_batch.types.eks_attempt_container_details.deserialize_json(
                data["initContainers"]
            )
        )
    if "eksClusterArn" in data:
        out["eks_cluster_arn"] = data["eksClusterArn"]
    if "podName" in data:
        out["pod_name"] = data["podName"]
    if "podNamespace" in data:
        out["pod_namespace"] = data["podNamespace"]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    if "startedAt" in data:
        out["started_at"] = data["startedAt"]
    if "stoppedAt" in data:
        out["stopped_at"] = data["stoppedAt"]
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
