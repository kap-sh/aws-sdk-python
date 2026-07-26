"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterKubernetesConfigNodeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_kubernetes_labels
    import capo_sagemaker.types.cluster_kubernetes_taints


class ClusterKubernetesConfigNodeDetails(TypedDict, closed=True):
    current_labels: NotRequired[
        "capo_sagemaker.types.cluster_kubernetes_labels.ClusterKubernetesLabels"
    ]
    """<p>The current labels applied to the cluster node.</p>"""
    desired_labels: NotRequired[
        "capo_sagemaker.types.cluster_kubernetes_labels.ClusterKubernetesLabels"
    ]
    """<p>The desired labels to be applied to the cluster node.</p>"""
    current_taints: NotRequired[
        "capo_sagemaker.types.cluster_kubernetes_taints.ClusterKubernetesTaints"
    ]
    """<p>The current taints applied to the cluster node.</p>"""
    desired_taints: NotRequired[
        "capo_sagemaker.types.cluster_kubernetes_taints.ClusterKubernetesTaints"
    ]
    """<p>The desired taints to be applied to the cluster node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterKubernetesConfigNodeDetails) -> dict:
    out: dict = {}
    if "current_labels" in value:
        import capo_sagemaker.types.cluster_kubernetes_labels

        out["CurrentLabels"] = (
            capo_sagemaker.types.cluster_kubernetes_labels.serialize_aws_json_1_1(
                value["current_labels"]
            )
        )
    if "desired_labels" in value:
        import capo_sagemaker.types.cluster_kubernetes_labels

        out["DesiredLabels"] = (
            capo_sagemaker.types.cluster_kubernetes_labels.serialize_aws_json_1_1(
                value["desired_labels"]
            )
        )
    if "current_taints" in value:
        import capo_sagemaker.types.cluster_kubernetes_taints

        out["CurrentTaints"] = (
            capo_sagemaker.types.cluster_kubernetes_taints.serialize_aws_json_1_1(
                value["current_taints"]
            )
        )
    if "desired_taints" in value:
        import capo_sagemaker.types.cluster_kubernetes_taints

        out["DesiredTaints"] = (
            capo_sagemaker.types.cluster_kubernetes_taints.serialize_aws_json_1_1(
                value["desired_taints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterKubernetesConfigNodeDetails:
    out: ClusterKubernetesConfigNodeDetails = {}  # type: ignore[typeddict-item]
    if "CurrentLabels" in data:
        import capo_sagemaker.types.cluster_kubernetes_labels

        out["current_labels"] = (
            capo_sagemaker.types.cluster_kubernetes_labels.deserialize_aws_json_1_1(
                data["CurrentLabels"]
            )
        )
    if "DesiredLabels" in data:
        import capo_sagemaker.types.cluster_kubernetes_labels

        out["desired_labels"] = (
            capo_sagemaker.types.cluster_kubernetes_labels.deserialize_aws_json_1_1(
                data["DesiredLabels"]
            )
        )
    if "CurrentTaints" in data:
        import capo_sagemaker.types.cluster_kubernetes_taints

        out["current_taints"] = (
            capo_sagemaker.types.cluster_kubernetes_taints.deserialize_aws_json_1_1(
                data["CurrentTaints"]
            )
        )
    if "DesiredTaints" in data:
        import capo_sagemaker.types.cluster_kubernetes_taints

        out["desired_taints"] = (
            capo_sagemaker.types.cluster_kubernetes_taints.deserialize_aws_json_1_1(
                data["DesiredTaints"]
            )
        )
    return out
