"""Generated from Smithy shape ``com.amazonaws.groundstation#CapabilityArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.capability_arn

CapabilityArnList: TypeAlias = list[
    "aws_sdk_groundstation.types.capability_arn.CapabilityArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> CapabilityArnList:
    return list(data)
