"""Generated from Smithy shape ``com.amazonaws.costexplorer#EBSResourceUtilization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class EBSResourceUtilization(TypedDict, closed=True):
    ebs_read_ops_per_second: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum number of read operations per second. </p>"""
    ebs_write_ops_per_second: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum number of write operations per second. </p>"""
    ebs_read_bytes_per_second: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum size of read operations per second </p>"""
    ebs_write_bytes_per_second: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum size of write operations per second. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EBSResourceUtilization) -> dict:
    out: dict = {}
    if "ebs_read_ops_per_second" in value:
        out["EbsReadOpsPerSecond"] = value["ebs_read_ops_per_second"]
    if "ebs_write_ops_per_second" in value:
        out["EbsWriteOpsPerSecond"] = value["ebs_write_ops_per_second"]
    if "ebs_read_bytes_per_second" in value:
        out["EbsReadBytesPerSecond"] = value["ebs_read_bytes_per_second"]
    if "ebs_write_bytes_per_second" in value:
        out["EbsWriteBytesPerSecond"] = value["ebs_write_bytes_per_second"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EBSResourceUtilization:
    out: EBSResourceUtilization = {}  # type: ignore[typeddict-item]
    if "EbsReadOpsPerSecond" in data:
        out["ebs_read_ops_per_second"] = data["EbsReadOpsPerSecond"]
    if "EbsWriteOpsPerSecond" in data:
        out["ebs_write_ops_per_second"] = data["EbsWriteOpsPerSecond"]
    if "EbsReadBytesPerSecond" in data:
        out["ebs_read_bytes_per_second"] = data["EbsReadBytesPerSecond"]
    if "EbsWriteBytesPerSecond" in data:
        out["ebs_write_bytes_per_second"] = data["EbsWriteBytesPerSecond"]
    return out
