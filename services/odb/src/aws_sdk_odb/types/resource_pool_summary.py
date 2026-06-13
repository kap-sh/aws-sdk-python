"""Generated from Smithy shape ``com.amazonaws.odb#ResourcePoolSummary``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ResourcePoolSummary(TypedDict):
    is_disabled: NotRequired["bool"]
    """<p>Indicates whether the resource pool is disabled.</p>"""
    pool_size: NotRequired["int"]
    """<p>The number of Autonomous Databases that the resource pool can contain.</p>"""
    pool_storage_size_in_t_bs: NotRequired["int"]
    """<p>The total storage size of the resource pool, in terabytes (TB).</p>"""
    available_storage_capacity_in_t_bs: NotRequired["float"]
    """<p>The available storage capacity in the resource pool, in TB.</p>"""
    total_compute_capacity: NotRequired["int"]
    """<p>The total compute capacity of the resource pool.</p>"""
    available_compute_capacity: NotRequired["int"]
    """<p>The available compute capacity in the resource pool.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourcePoolSummary) -> dict:
    out: dict = {}
    if "is_disabled" in value:
        out["isDisabled"] = value["is_disabled"]
    if "pool_size" in value:
        out["poolSize"] = value["pool_size"]
    if "pool_storage_size_in_t_bs" in value:
        out["poolStorageSizeInTBs"] = value["pool_storage_size_in_t_bs"]
    if "available_storage_capacity_in_t_bs" in value:
        out["availableStorageCapacityInTBs"] = value[
            "available_storage_capacity_in_t_bs"
        ]
    if "total_compute_capacity" in value:
        out["totalComputeCapacity"] = value["total_compute_capacity"]
    if "available_compute_capacity" in value:
        out["availableComputeCapacity"] = value["available_compute_capacity"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourcePoolSummary:
    out: ResourcePoolSummary = {}  # type: ignore[typeddict-item]
    if "isDisabled" in data:
        out["is_disabled"] = data["isDisabled"]
    if "poolSize" in data:
        out["pool_size"] = data["poolSize"]
    if "poolStorageSizeInTBs" in data:
        out["pool_storage_size_in_t_bs"] = data["poolStorageSizeInTBs"]
    if "availableStorageCapacityInTBs" in data:
        out["available_storage_capacity_in_t_bs"] = data[
            "availableStorageCapacityInTBs"
        ]
    if "totalComputeCapacity" in data:
        out["total_compute_capacity"] = data["totalComputeCapacity"]
    if "availableComputeCapacity" in data:
        out["available_compute_capacity"] = data["availableComputeCapacity"]
    return out
