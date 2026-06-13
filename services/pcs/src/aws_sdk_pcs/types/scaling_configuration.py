"""Generated from Smithy shape ``com.amazonaws.pcs#ScalingConfiguration``."""

from typing import TypedDict


class ScalingConfiguration(TypedDict):
    min_instance_count: "int"
    """<p>The lower bound of the number of instances allowed in the compute fleet.</p>"""
    max_instance_count: "int"
    """<p>The upper bound of the number of instances allowed in the compute fleet.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScalingConfiguration) -> dict:
    out: dict = {}
    out["minInstanceCount"] = value.get("min_instance_count", 0)
    out["maxInstanceCount"] = value.get("max_instance_count", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> ScalingConfiguration:
    out: ScalingConfiguration = {}  # type: ignore[typeddict-item]
    if "minInstanceCount" in data:
        out["min_instance_count"] = data["minInstanceCount"]
    else:
        out["min_instance_count"] = 0
    if "maxInstanceCount" in data:
        out["max_instance_count"] = data["maxInstanceCount"]
    else:
        out["max_instance_count"] = 0
    return out
