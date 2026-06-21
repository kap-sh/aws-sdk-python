"""Generated from Smithy shape ``com.amazonaws.securityhub#Partition``."""

from typing import Literal, TypeAlias, cast

Partition: TypeAlias = Literal[
    "aws",
    "aws-cn",
    "aws-us-gov",
]


# --- restJson1 ser/de ---
def serialize_json(value: Partition) -> str:
    return value


def deserialize_json(data: str) -> Partition:
    return cast(Partition, data)
