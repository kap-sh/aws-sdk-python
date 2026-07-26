"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOrchestratorEksConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.eks_cluster_arn


class ClusterOrchestratorEksConfig(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_sagemaker.types.eks_cluster_arn.EksClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon EKS cluster associated with the SageMaker HyperPod cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOrchestratorEksConfig) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterOrchestratorEksConfig:
    out: ClusterOrchestratorEksConfig = {}  # type: ignore[typeddict-item]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    return out
