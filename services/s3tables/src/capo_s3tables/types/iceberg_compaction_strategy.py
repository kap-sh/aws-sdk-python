"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergCompactionStrategy``."""

from typing import Literal, TypeAlias, cast

IcebergCompactionStrategy: TypeAlias = Literal[
    "auto",
    "binpack",
    "sort",
    "z-order",
]


# --- restJson1 ser/de ---
def serialize_json(value: IcebergCompactionStrategy) -> str:
    return value


def deserialize_json(data: str) -> IcebergCompactionStrategy:
    return cast(IcebergCompactionStrategy, data)
