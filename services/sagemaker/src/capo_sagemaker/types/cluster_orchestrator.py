"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOrchestrator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_orchestrator_eks_config
    import capo_sagemaker.types.cluster_orchestrator_slurm_config


class ClusterOrchestrator(TypedDict, closed=True):
    eks: NotRequired[
        "capo_sagemaker.types.cluster_orchestrator_eks_config.ClusterOrchestratorEksConfig"
    ]
    """<p>The Amazon EKS cluster used as the orchestrator for the SageMaker HyperPod cluster.</p>"""
    slurm: NotRequired[
        "capo_sagemaker.types.cluster_orchestrator_slurm_config.ClusterOrchestratorSlurmConfig"
    ]
    """<p>The Slurm orchestrator configuration for the SageMaker HyperPod cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOrchestrator) -> dict:
    out: dict = {}
    if "eks" in value:
        import capo_sagemaker.types.cluster_orchestrator_eks_config

        out["Eks"] = (
            capo_sagemaker.types.cluster_orchestrator_eks_config.serialize_aws_json_1_1(
                value["eks"]
            )
        )
    if "slurm" in value:
        import capo_sagemaker.types.cluster_orchestrator_slurm_config

        out["Slurm"] = (
            capo_sagemaker.types.cluster_orchestrator_slurm_config.serialize_aws_json_1_1(
                value["slurm"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterOrchestrator:
    out: ClusterOrchestrator = {}  # type: ignore[typeddict-item]
    if "Eks" in data:
        import capo_sagemaker.types.cluster_orchestrator_eks_config

        out["eks"] = (
            capo_sagemaker.types.cluster_orchestrator_eks_config.deserialize_aws_json_1_1(
                data["Eks"]
            )
        )
    if "Slurm" in data:
        import capo_sagemaker.types.cluster_orchestrator_slurm_config

        out["slurm"] = (
            capo_sagemaker.types.cluster_orchestrator_slurm_config.deserialize_aws_json_1_1(
                data["Slurm"]
            )
        )
    return out
