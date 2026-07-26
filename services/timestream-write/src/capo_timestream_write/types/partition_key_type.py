"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#PartitionKeyType``."""

from typing import Literal, TypeAlias, cast

PartitionKeyType: TypeAlias = Literal[
    "DIMENSION",
    "MEASURE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartitionKeyType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PartitionKeyType:
    return cast(PartitionKeyType, data)
