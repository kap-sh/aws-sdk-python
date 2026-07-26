"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterTieredStorageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_config_mode
    import capo_sagemaker.types.cluster_instance_memory_allocation_percentage


class ClusterTieredStorageConfig(TypedDict, closed=True):
    mode: NotRequired["capo_sagemaker.types.cluster_config_mode.ClusterConfigMode"]
    """<p>Specifies whether managed tier checkpointing is enabled or disabled for the HyperPod cluster. When set to <code>Enable</code>, the system installs a memory management daemon that provides disaggregated memory as a service for checkpoint storage. When set to <code>Disable</code>, the feature is turned off and the memory management daemon is removed from the cluster.</p>"""
    instance_memory_allocation_percentage: NotRequired[
        "capo_sagemaker.types.cluster_instance_memory_allocation_percentage.ClusterInstanceMemoryAllocationPercentage"
    ]
    """<p>The percentage (int) of cluster memory to allocate for checkpointing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterTieredStorageConfig) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_sagemaker.types.cluster_config_mode

        out["Mode"] = capo_sagemaker.types.cluster_config_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    if "instance_memory_allocation_percentage" in value:
        out["InstanceMemoryAllocationPercentage"] = value[
            "instance_memory_allocation_percentage"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterTieredStorageConfig:
    out: ClusterTieredStorageConfig = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import capo_sagemaker.types.cluster_config_mode

        out["mode"] = capo_sagemaker.types.cluster_config_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    if "InstanceMemoryAllocationPercentage" in data:
        out["instance_memory_allocation_percentage"] = data[
            "InstanceMemoryAllocationPercentage"
        ]
    return out
