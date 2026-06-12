"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsEksWorkloadInfo``."""

from typing import TypedDict
from aws_sdk_inspector2.errors import DeserializationError

class AwsEksWorkloadInfo(TypedDict):
    name: "str"
    """<p>The name of the workload.</p>"""
    type: "str"
    """<p>The workload type.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AwsEksWorkloadInfo) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsEksWorkloadInfo:
    out: AwsEksWorkloadInfo = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AwsEksWorkloadInfo.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AwsEksWorkloadInfo.type required")
    return out