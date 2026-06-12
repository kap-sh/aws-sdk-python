"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterKubernetesLabels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_kubernetes_label_key
    import aws_sdk_sagemaker.types.cluster_kubernetes_label_value

ClusterKubernetesLabels: TypeAlias = dict[
    "aws_sdk_sagemaker.types.cluster_kubernetes_label_key.ClusterKubernetesLabelKey",
    "aws_sdk_sagemaker.types.cluster_kubernetes_label_value.ClusterKubernetesLabelValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ClusterKubernetesLabels) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterKubernetesLabels:
    out: ClusterKubernetesLabels = {}
    for key, value in data.items():
        out[key] = value
    return out
