"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#BlockStoragePerformanceConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class BlockStoragePerformanceConfiguration(TypedDict, closed=True):
    iops: NotRequired["float"]
    """<p>The number of I/O operations per second.</p>"""
    throughput: NotRequired["float"]
    """<p>The throughput that the volume supports.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BlockStoragePerformanceConfiguration) -> dict:
    out: dict = {}
    if "iops" in value:
        out["iops"] = value["iops"]
    if "throughput" in value:
        out["throughput"] = value["throughput"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BlockStoragePerformanceConfiguration:
    out: BlockStoragePerformanceConfiguration = {}  # type: ignore[typeddict-item]
    if "iops" in data:
        out["iops"] = data["iops"]
    if "throughput" in data:
        out["throughput"] = data["throughput"]
    return out
