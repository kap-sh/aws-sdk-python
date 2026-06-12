"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#CpuOptions``."""

from typing import TypedDict
from typing_extensions import NotRequired

class CpuOptions(TypedDict):
    core_count: NotRequired["int"]
    """<p>The number of cores that the CPU can use.</p>"""
    threads_per_core: NotRequired["int"]
    """<p>The number of threads per core in the CPU.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CpuOptions) -> dict:
    out: dict = {}
    if "core_count" in value:
        out["coreCount"] = value["core_count"]
    if "threads_per_core" in value:
        out["threadsPerCore"] = value["threads_per_core"]
    return out


def deserialize_json(data: dict) -> CpuOptions:
    out: CpuOptions = {}  # type: ignore[typeddict-item]
    if "coreCount" in data:
        out["core_count"] = data["coreCount"]
    if "threadsPerCore" in data:
        out["threads_per_core"] = data["threadsPerCore"]
    return out