"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceStorageConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_instance_storage_config

ClusterInstanceStorageConfigs: TypeAlias = list[
    "capo_sagemaker.types.cluster_instance_storage_config.ClusterInstanceStorageConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceStorageConfigs) -> list:
    import capo_sagemaker.types.cluster_instance_storage_config

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.cluster_instance_storage_config.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterInstanceStorageConfigs:
    import capo_sagemaker.types.cluster_instance_storage_config

    out: ClusterInstanceStorageConfigs = []
    for item in data:
        out.append(
            capo_sagemaker.types.cluster_instance_storage_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
