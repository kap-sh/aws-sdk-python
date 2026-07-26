"""Generated from Smithy shape ``com.amazonaws.emrserverless#TotalResourceUtilization``."""

from typing_extensions import NotRequired, TypedDict


class TotalResourceUtilization(TypedDict, closed=True):
    v_cpu_hour: NotRequired["float"]
    """<p>The aggregated vCPU used per hour from the time job start executing till the time job is terminated.</p>"""
    memory_gb_hour: NotRequired["float"]
    """<p>The aggregated memory used per hour from the time job start executing till the time job is terminated.</p>"""
    storage_gb_hour: NotRequired["float"]
    """<p>The aggregated storage used per hour from the time job start executing till the time job is terminated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TotalResourceUtilization) -> dict:
    out: dict = {}
    if "v_cpu_hour" in value:
        out["vCPUHour"] = value["v_cpu_hour"]
    if "memory_gb_hour" in value:
        out["memoryGBHour"] = value["memory_gb_hour"]
    if "storage_gb_hour" in value:
        out["storageGBHour"] = value["storage_gb_hour"]
    return out


def deserialize_json(data: dict) -> TotalResourceUtilization:
    out: TotalResourceUtilization = {}  # type: ignore[typeddict-item]
    if "vCPUHour" in data:
        out["v_cpu_hour"] = data["vCPUHour"]
    if "memoryGBHour" in data:
        out["memory_gb_hour"] = data["memoryGBHour"]
    if "storageGBHour" in data:
        out["storage_gb_hour"] = data["storageGBHour"]
    return out
