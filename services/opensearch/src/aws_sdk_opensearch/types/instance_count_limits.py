"""Generated from Smithy shape ``com.amazonaws.opensearch#InstanceCountLimits``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.maximum_instance_count
    import aws_sdk_opensearch.types.minimum_instance_count


class InstanceCountLimits(TypedDict):
    minimum_instance_count: (
        "aws_sdk_opensearch.types.minimum_instance_count.MinimumInstanceCount"
    )
    """<p>The maximum allowed number of instances.</p>"""
    maximum_instance_count: (
        "aws_sdk_opensearch.types.maximum_instance_count.MaximumInstanceCount"
    )
    """<p>The minimum allowed number of instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceCountLimits) -> dict:
    out: dict = {}
    out["MinimumInstanceCount"] = value.get("minimum_instance_count", 0)
    out["MaximumInstanceCount"] = value.get("maximum_instance_count", 0)
    return out


def deserialize_json(data: dict) -> InstanceCountLimits:
    out: InstanceCountLimits = {}  # type: ignore[typeddict-item]
    if "MinimumInstanceCount" in data:
        out["minimum_instance_count"] = data["MinimumInstanceCount"]
    else:
        out["minimum_instance_count"] = 0
    if "MaximumInstanceCount" in data:
        out["maximum_instance_count"] = data["MaximumInstanceCount"]
    else:
        out["maximum_instance_count"] = 0
    return out
