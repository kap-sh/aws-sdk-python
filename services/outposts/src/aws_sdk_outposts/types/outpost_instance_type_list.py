"""Generated from Smithy shape ``com.amazonaws.outposts#OutpostInstanceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.outpost_instance_type

OutpostInstanceTypeList: TypeAlias = list[
    "aws_sdk_outposts.types.outpost_instance_type.OutpostInstanceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutpostInstanceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> OutpostInstanceTypeList:
    return list(data)
