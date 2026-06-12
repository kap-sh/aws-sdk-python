"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#InstanceCountLimits``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.maximum_instance_count
    import aws_sdk_elasticsearch_service.types.minimum_instance_count


class InstanceCountLimits(TypedDict):
    minimum_instance_count: "aws_sdk_elasticsearch_service.types.minimum_instance_count.MinimumInstanceCount"
    maximum_instance_count: "aws_sdk_elasticsearch_service.types.maximum_instance_count.MaximumInstanceCount"


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
