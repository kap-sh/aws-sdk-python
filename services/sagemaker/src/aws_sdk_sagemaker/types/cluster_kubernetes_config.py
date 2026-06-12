"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterKubernetesConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_kubernetes_labels
    import aws_sdk_sagemaker.types.cluster_kubernetes_taints


class ClusterKubernetesConfig(TypedDict):
    labels: NotRequired[
        "aws_sdk_sagemaker.types.cluster_kubernetes_labels.ClusterKubernetesLabels"
    ]
    """<p>Key-value pairs of labels to be applied to cluster nodes.</p>"""
    taints: NotRequired[
        "aws_sdk_sagemaker.types.cluster_kubernetes_taints.ClusterKubernetesTaints"
    ]
    """<p>List of taints to be applied to cluster nodes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterKubernetesConfig) -> dict:
    out: dict = {}
    if "labels" in value:
        import aws_sdk_sagemaker.types.cluster_kubernetes_labels

        out["Labels"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_labels.serialize_aws_json_1_1(
                value["labels"]
            )
        )
    if "taints" in value:
        import aws_sdk_sagemaker.types.cluster_kubernetes_taints

        out["Taints"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_taints.serialize_aws_json_1_1(
                value["taints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterKubernetesConfig:
    out: ClusterKubernetesConfig = {}  # type: ignore[typeddict-item]
    if "Labels" in data:
        import aws_sdk_sagemaker.types.cluster_kubernetes_labels

        out["labels"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_labels.deserialize_aws_json_1_1(
                data["Labels"]
            )
        )
    if "Taints" in data:
        import aws_sdk_sagemaker.types.cluster_kubernetes_taints

        out["taints"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_taints.deserialize_aws_json_1_1(
                data["Taints"]
            )
        )
    return out
