"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOrchestratorSlurmConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_slurm_config_strategy


class ClusterOrchestratorSlurmConfig(TypedDict):
    slurm_config_strategy: NotRequired[
        "aws_sdk_sagemaker.types.cluster_slurm_config_strategy.ClusterSlurmConfigStrategy"
    ]
    """<p>The strategy for managing partitions for the Slurm configuration. Valid values are <code>Managed</code>, <code>Overwrite</code>, and <code>Merge</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOrchestratorSlurmConfig) -> dict:
    out: dict = {}
    if "slurm_config_strategy" in value:
        import aws_sdk_sagemaker.types.cluster_slurm_config_strategy

        out["SlurmConfigStrategy"] = (
            aws_sdk_sagemaker.types.cluster_slurm_config_strategy.serialize_aws_json_1_1(
                value["slurm_config_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterOrchestratorSlurmConfig:
    out: ClusterOrchestratorSlurmConfig = {}  # type: ignore[typeddict-item]
    if "SlurmConfigStrategy" in data:
        import aws_sdk_sagemaker.types.cluster_slurm_config_strategy

        out["slurm_config_strategy"] = (
            aws_sdk_sagemaker.types.cluster_slurm_config_strategy.deserialize_aws_json_1_1(
                data["SlurmConfigStrategy"]
            )
        )
    return out
