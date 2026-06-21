"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#Compression``."""

from typing import Literal, TypeAlias, cast

Compression: TypeAlias = Literal[
    "OFF",
    "SNAPPY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Compression) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Compression:
    return cast(Compression, data)
