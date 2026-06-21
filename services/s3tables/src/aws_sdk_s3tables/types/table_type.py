"""Generated from Smithy shape ``com.amazonaws.s3tables#TableType``."""

from typing import Literal, TypeAlias, cast

TableType: TypeAlias = Literal[
    "customer",
    "aws",
]


# --- restJson1 ser/de ---
def serialize_json(value: TableType) -> str:
    return value


def deserialize_json(data: str) -> TableType:
    return cast(TableType, data)
