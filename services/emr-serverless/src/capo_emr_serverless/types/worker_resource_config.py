"""Generated from Smithy shape ``com.amazonaws.emrserverless#WorkerResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_serverless.types.cpu_size
    import capo_emr_serverless.types.disk_size
    import capo_emr_serverless.types.disk_type
    import capo_emr_serverless.types.memory_size


class WorkerResourceConfig(TypedDict, closed=True):
    cpu: "capo_emr_serverless.types.cpu_size.CpuSize"
    """<p>The CPU requirements for every worker instance of the worker type.</p>"""
    memory: "capo_emr_serverless.types.memory_size.MemorySize"
    """<p>The memory requirements for every worker instance of the worker type.</p>"""
    disk: NotRequired["capo_emr_serverless.types.disk_size.DiskSize"]
    """<p>The disk requirements for every worker instance of the worker type.</p>"""
    disk_type: NotRequired["capo_emr_serverless.types.disk_type.DiskType"]
    """<p>The disk type for every worker instance of the work type. Shuffle optimized disks have higher performance characteristics and are better for shuffle heavy workloads. Default is <code>STANDARD</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerResourceConfig) -> dict:
    out: dict = {}
    out["cpu"] = value["cpu"]
    out["memory"] = value["memory"]
    if "disk" in value:
        out["disk"] = value["disk"]
    if "disk_type" in value:
        out["diskType"] = value["disk_type"]
    return out


def deserialize_json(data: dict) -> WorkerResourceConfig:
    out: WorkerResourceConfig = {}  # type: ignore[typeddict-item]
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    else:
        raise DeserializationError("WorkerResourceConfig.cpu required")
    if "memory" in data:
        out["memory"] = data["memory"]
    else:
        raise DeserializationError("WorkerResourceConfig.memory required")
    if "disk" in data:
        out["disk"] = data["disk"]
    if "diskType" in data:
        out["disk_type"] = data["diskType"]
    return out
