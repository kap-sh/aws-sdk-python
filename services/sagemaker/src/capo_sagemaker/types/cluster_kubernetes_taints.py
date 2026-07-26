"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterKubernetesTaints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_kubernetes_taint

ClusterKubernetesTaints: TypeAlias = list[
    "capo_sagemaker.types.cluster_kubernetes_taint.ClusterKubernetesTaint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterKubernetesTaints) -> list:
    import capo_sagemaker.types.cluster_kubernetes_taint

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.cluster_kubernetes_taint.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterKubernetesTaints:
    import capo_sagemaker.types.cluster_kubernetes_taint

    out: ClusterKubernetesTaints = []
    for item in data:
        out.append(
            capo_sagemaker.types.cluster_kubernetes_taint.deserialize_aws_json_1_1(item)
        )
    return out
