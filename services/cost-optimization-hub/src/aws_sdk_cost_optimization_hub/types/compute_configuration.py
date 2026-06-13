"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ComputeConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ComputeConfiguration(TypedDict):
    v_cpu: NotRequired["float"]
    """<p>The number of vCPU cores in the resource.</p>"""
    memory_size_in_mb: NotRequired["int"]
    """<p>The memory size of the resource.</p>"""
    architecture: NotRequired["str"]
    """<p>The architecture of the resource.</p>"""
    platform: NotRequired["str"]
    """<p>The platform of the resource. The platform is the specific combination of operating system, license model, and software on an instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeConfiguration) -> dict:
    out: dict = {}
    if "v_cpu" in value:
        out["vCpu"] = value["v_cpu"]
    if "memory_size_in_mb" in value:
        out["memorySizeInMB"] = value["memory_size_in_mb"]
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    if "platform" in value:
        out["platform"] = value["platform"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ComputeConfiguration:
    out: ComputeConfiguration = {}  # type: ignore[typeddict-item]
    if "vCpu" in data:
        out["v_cpu"] = data["vCpu"]
    if "memorySizeInMB" in data:
        out["memory_size_in_mb"] = data["memorySizeInMB"]
    if "architecture" in data:
        out["architecture"] = data["architecture"]
    if "platform" in data:
        out["platform"] = data["platform"]
    return out
