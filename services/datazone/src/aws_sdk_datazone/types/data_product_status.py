"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductStatus``."""

from typing import Literal, TypeAlias, cast

DataProductStatus: TypeAlias = Literal[
    "CREATED",
    "CREATING",
    "CREATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataProductStatus) -> str:
    return value


def deserialize_json(data: str) -> DataProductStatus:
    return cast(DataProductStatus, data)
