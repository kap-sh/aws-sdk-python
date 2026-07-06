"""Generated from Smithy shape ``com.amazonaws.costexplorer#DiskResourceUtilization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class DiskResourceUtilization(TypedDict, closed=True):
    disk_read_ops_per_second: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum number of read operations per second. </p>"""
    disk_write_ops_per_second: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum number of write operations per second. </p>"""
    disk_read_bytes_per_second: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum read throughput operations per second. </p>"""
    disk_write_bytes_per_second: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum write throughput operations per second. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskResourceUtilization) -> dict:
    out: dict = {}
    if "disk_read_ops_per_second" in value:
        out["DiskReadOpsPerSecond"] = value["disk_read_ops_per_second"]
    if "disk_write_ops_per_second" in value:
        out["DiskWriteOpsPerSecond"] = value["disk_write_ops_per_second"]
    if "disk_read_bytes_per_second" in value:
        out["DiskReadBytesPerSecond"] = value["disk_read_bytes_per_second"]
    if "disk_write_bytes_per_second" in value:
        out["DiskWriteBytesPerSecond"] = value["disk_write_bytes_per_second"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiskResourceUtilization:
    out: DiskResourceUtilization = {}  # type: ignore[typeddict-item]
    if "DiskReadOpsPerSecond" in data:
        out["disk_read_ops_per_second"] = data["DiskReadOpsPerSecond"]
    if "DiskWriteOpsPerSecond" in data:
        out["disk_write_ops_per_second"] = data["DiskWriteOpsPerSecond"]
    if "DiskReadBytesPerSecond" in data:
        out["disk_read_bytes_per_second"] = data["DiskReadBytesPerSecond"]
    if "DiskWriteBytesPerSecond" in data:
        out["disk_write_bytes_per_second"] = data["DiskWriteBytesPerSecond"]
    return out
