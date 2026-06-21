"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergNullOrder``."""

from typing import Literal, TypeAlias, cast

IcebergNullOrder: TypeAlias = Literal[
    "nulls-first",
    "nulls-last",
]


# --- restJson1 ser/de ---
def serialize_json(value: IcebergNullOrder) -> str:
    return value


def deserialize_json(data: str) -> IcebergNullOrder:
    return cast(IcebergNullOrder, data)
