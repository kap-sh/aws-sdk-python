"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergSortDirection``."""

from typing import Literal, TypeAlias, cast

IcebergSortDirection: TypeAlias = Literal[
    "asc",
    "desc",
]


# --- restJson1 ser/de ---
def serialize_json(value: IcebergSortDirection) -> str:
    return value


def deserialize_json(data: str) -> IcebergSortDirection:
    return cast(IcebergSortDirection, data)
