"""Generated from Smithy shape ``com.amazonaws.b2bi#CapabilityType``."""

from typing import Literal, TypeAlias, cast

CapabilityType: TypeAlias = Literal["edi",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapabilityType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CapabilityType:
    return cast(CapabilityType, data)
