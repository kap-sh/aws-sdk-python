"""Generated from Smithy shape ``com.amazonaws.batch#CapacityLimits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.capacity_limit

CapacityLimits: TypeAlias = list["aws_sdk_batch.types.capacity_limit.CapacityLimit"]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityLimits) -> list:
    import aws_sdk_batch.types.capacity_limit

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.capacity_limit.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapacityLimits:
    import aws_sdk_batch.types.capacity_limit

    out: CapacityLimits = []
    for item in data:
        out.append(aws_sdk_batch.types.capacity_limit.deserialize_json(item))
    return out
