"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSlurmConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_partition_names
    import aws_sdk_sagemaker.types.cluster_slurm_node_type


class ClusterSlurmConfig(TypedDict, closed=True):
    node_type: "aws_sdk_sagemaker.types.cluster_slurm_node_type.ClusterSlurmNodeType"
    """<p>The type of Slurm node for the instance group. Valid values are <code>Controller</code>, <code>Worker</code>, and <code>Login</code>.</p>"""
    partition_names: NotRequired[
        "aws_sdk_sagemaker.types.cluster_partition_names.ClusterPartitionNames"
    ]
    """<p>The list of Slurm partition names that the instance group belongs to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSlurmConfig) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker.types.cluster_slurm_node_type

    out["NodeType"] = (
        aws_sdk_sagemaker.types.cluster_slurm_node_type.serialize_aws_json_1_1(
            value["node_type"]
        )
    )
    if "partition_names" in value:
        import aws_sdk_sagemaker.types.cluster_partition_names

        out["PartitionNames"] = (
            aws_sdk_sagemaker.types.cluster_partition_names.serialize_aws_json_1_1(
                value["partition_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterSlurmConfig:
    out: ClusterSlurmConfig = {}  # type: ignore[typeddict-item]
    if "NodeType" in data:
        import aws_sdk_sagemaker.types.cluster_slurm_node_type

        out["node_type"] = (
            aws_sdk_sagemaker.types.cluster_slurm_node_type.deserialize_aws_json_1_1(
                data["NodeType"]
            )
        )
    else:
        raise DeserializationError("ClusterSlurmConfig.node_type required")
    if "PartitionNames" in data:
        import aws_sdk_sagemaker.types.cluster_partition_names

        out["partition_names"] = (
            aws_sdk_sagemaker.types.cluster_partition_names.deserialize_aws_json_1_1(
                data["PartitionNames"]
            )
        )
    return out
