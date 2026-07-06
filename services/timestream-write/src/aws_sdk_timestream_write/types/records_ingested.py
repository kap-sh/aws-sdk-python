"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#RecordsIngested``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.integer


class RecordsIngested(TypedDict, closed=True):
    total: "aws_sdk_timestream_write.types.integer.Integer"
    """<p>Total count of successfully ingested records.</p>"""
    memory_store: "aws_sdk_timestream_write.types.integer.Integer"
    """<p>Count of records ingested into the memory store.</p>"""
    magnetic_store: "aws_sdk_timestream_write.types.integer.Integer"
    """<p>Count of records ingested into the magnetic store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecordsIngested) -> dict:
    out: dict = {}
    out["Total"] = value.get("total", 0)
    out["MemoryStore"] = value.get("memory_store", 0)
    out["MagneticStore"] = value.get("magnetic_store", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> RecordsIngested:
    out: RecordsIngested = {}  # type: ignore[typeddict-item]
    if "Total" in data:
        out["total"] = data["Total"]
    else:
        out["total"] = 0
    if "MemoryStore" in data:
        out["memory_store"] = data["MemoryStore"]
    else:
        out["memory_store"] = 0
    if "MagneticStore" in data:
        out["magnetic_store"] = data["MagneticStore"]
    else:
        out["magnetic_store"] = 0
    return out
