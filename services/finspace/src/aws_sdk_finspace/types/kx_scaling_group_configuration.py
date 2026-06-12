"""Generated from Smithy shape ``com.amazonaws.finspace#KxScalingGroupConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.cluster_node_count
    import aws_sdk_finspace.types.cpu_count
    import aws_sdk_finspace.types.kx_scaling_group_name
    import aws_sdk_finspace.types.memory_mib


class KxScalingGroupConfiguration(TypedDict):
    scaling_group_name: (
        "aws_sdk_finspace.types.kx_scaling_group_name.KxScalingGroupName"
    )
    """<p>A unique identifier for the kdb scaling group. </p>"""
    memory_limit: NotRequired["aws_sdk_finspace.types.memory_mib.MemoryMib"]
    """<p> An optional hard limit on the amount of memory a kdb cluster can use. </p>"""
    memory_reservation: "aws_sdk_finspace.types.memory_mib.MemoryMib"
    """<p> A reservation of the minimum amount of memory that should be available on the scaling group for a kdb cluster to be successfully placed in a scaling group. </p>"""
    node_count: "aws_sdk_finspace.types.cluster_node_count.ClusterNodeCount"
    """<p> The number of kdb cluster nodes. </p>"""
    cpu: NotRequired["aws_sdk_finspace.types.cpu_count.CpuCount"]
    """<p> The number of vCPUs that you want to reserve for each node of this kdb cluster on the scaling group host. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxScalingGroupConfiguration) -> dict:
    out: dict = {}
    out["scalingGroupName"] = value["scaling_group_name"]
    if "memory_limit" in value:
        out["memoryLimit"] = value["memory_limit"]
    out["memoryReservation"] = value["memory_reservation"]
    out["nodeCount"] = value["node_count"]
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    return out


def deserialize_json(data: dict) -> KxScalingGroupConfiguration:
    out: KxScalingGroupConfiguration = {}  # type: ignore[typeddict-item]
    if "scalingGroupName" in data:
        out["scaling_group_name"] = data["scalingGroupName"]
    else:
        raise DeserializationError(
            "KxScalingGroupConfiguration.scaling_group_name required"
        )
    if "memoryLimit" in data:
        out["memory_limit"] = data["memoryLimit"]
    if "memoryReservation" in data:
        out["memory_reservation"] = data["memoryReservation"]
    else:
        raise DeserializationError(
            "KxScalingGroupConfiguration.memory_reservation required"
        )
    if "nodeCount" in data:
        out["node_count"] = data["nodeCount"]
    else:
        raise DeserializationError("KxScalingGroupConfiguration.node_count required")
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    return out
