"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterKubernetesConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_kubernetes_labels
    import aws_sdk_sagemaker.types.cluster_kubernetes_taints


class ClusterKubernetesConfigDetails(TypedDict, closed=True):
    current_labels: NotRequired[
        "aws_sdk_sagemaker.types.cluster_kubernetes_labels.ClusterKubernetesLabels"
    ]
    """<p>The current labels applied to cluster nodes of an instance group.</p>"""
    desired_labels: NotRequired[
        "aws_sdk_sagemaker.types.cluster_kubernetes_labels.ClusterKubernetesLabels"
    ]
    """<p>The desired labels to be applied to cluster nodes of an instance group.</p>"""
    current_taints: NotRequired[
        "aws_sdk_sagemaker.types.cluster_kubernetes_taints.ClusterKubernetesTaints"
    ]
    """<p>The current taints applied to cluster nodes of an instance group.</p>"""
    desired_taints: NotRequired[
        "aws_sdk_sagemaker.types.cluster_kubernetes_taints.ClusterKubernetesTaints"
    ]
    """<p>The desired taints to be applied to cluster nodes of an instance group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterKubernetesConfigDetails) -> dict:
    out: dict = {}
    if "current_labels" in value:
        import aws_sdk_sagemaker.types.cluster_kubernetes_labels

        out["CurrentLabels"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_labels.serialize_aws_json_1_1(
                value["current_labels"]
            )
        )
    if "desired_labels" in value:
        import aws_sdk_sagemaker.types.cluster_kubernetes_labels

        out["DesiredLabels"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_labels.serialize_aws_json_1_1(
                value["desired_labels"]
            )
        )
    if "current_taints" in value:
        import aws_sdk_sagemaker.types.cluster_kubernetes_taints

        out["CurrentTaints"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_taints.serialize_aws_json_1_1(
                value["current_taints"]
            )
        )
    if "desired_taints" in value:
        import aws_sdk_sagemaker.types.cluster_kubernetes_taints

        out["DesiredTaints"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_taints.serialize_aws_json_1_1(
                value["desired_taints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterKubernetesConfigDetails:
    out: ClusterKubernetesConfigDetails = {}  # type: ignore[typeddict-item]
    if "CurrentLabels" in data:
        import aws_sdk_sagemaker.types.cluster_kubernetes_labels

        out["current_labels"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_labels.deserialize_aws_json_1_1(
                data["CurrentLabels"]
            )
        )
    if "DesiredLabels" in data:
        import aws_sdk_sagemaker.types.cluster_kubernetes_labels

        out["desired_labels"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_labels.deserialize_aws_json_1_1(
                data["DesiredLabels"]
            )
        )
    if "CurrentTaints" in data:
        import aws_sdk_sagemaker.types.cluster_kubernetes_taints

        out["current_taints"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_taints.deserialize_aws_json_1_1(
                data["CurrentTaints"]
            )
        )
    if "DesiredTaints" in data:
        import aws_sdk_sagemaker.types.cluster_kubernetes_taints

        out["desired_taints"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_taints.deserialize_aws_json_1_1(
                data["DesiredTaints"]
            )
        )
    return out
