"""Generated from Smithy shape ``com.amazonaws.evs#InstanceType``."""

from typing import Literal, TypeAlias, cast

InstanceType: TypeAlias = Literal[
    "i4i.metal",
    "i7i.metal-24xl",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceType:
    return cast(InstanceType, data)
