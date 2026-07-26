"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalValueType``."""

from typing import Literal, TypeAlias, cast

SignalValueType: TypeAlias = Literal[
    "INTEGER",
    "FLOATING_POINT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalValueType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SignalValueType:
    return cast(SignalValueType, data)
