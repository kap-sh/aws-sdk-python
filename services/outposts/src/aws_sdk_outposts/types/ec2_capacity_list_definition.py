"""Generated from Smithy shape ``com.amazonaws.outposts#EC2CapacityListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.ec2_capacity

EC2CapacityListDefinition: TypeAlias = list[
    "aws_sdk_outposts.types.ec2_capacity.EC2Capacity"
]


# --- restJson1 ser/de ---
def serialize_json(value: EC2CapacityListDefinition) -> list:
    import aws_sdk_outposts.types.ec2_capacity

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.ec2_capacity.serialize_json(item))
    return out


def deserialize_json(data: list) -> EC2CapacityListDefinition:
    import aws_sdk_outposts.types.ec2_capacity

    out: EC2CapacityListDefinition = []
    for item in data:
        out.append(aws_sdk_outposts.types.ec2_capacity.deserialize_json(item))
    return out
