"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketType``."""

from typing import Literal, TypeAlias, cast

TableBucketType: TypeAlias = Literal[
    "customer",
    "aws",
]


# --- restJson1 ser/de ---
def serialize_json(value: TableBucketType) -> str:
    return value


def deserialize_json(data: str) -> TableBucketType:
    return cast(TableBucketType, data)
