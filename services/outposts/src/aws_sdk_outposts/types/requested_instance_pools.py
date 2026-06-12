"""Generated from Smithy shape ``com.amazonaws.outposts#RequestedInstancePools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.instance_type_capacity

RequestedInstancePools: TypeAlias = list[
    "aws_sdk_outposts.types.instance_type_capacity.InstanceTypeCapacity"
]


# --- restJson1 ser/de ---
def serialize_json(value: RequestedInstancePools) -> list:
    import aws_sdk_outposts.types.instance_type_capacity

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.instance_type_capacity.serialize_json(item))
    return out


def deserialize_json(data: list) -> RequestedInstancePools:
    import aws_sdk_outposts.types.instance_type_capacity

    out: RequestedInstancePools = []
    for item in data:
        out.append(aws_sdk_outposts.types.instance_type_capacity.deserialize_json(item))
    return out
