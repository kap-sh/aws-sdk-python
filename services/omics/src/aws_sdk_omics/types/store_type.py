"""Generated from Smithy shape ``com.amazonaws.omics#StoreType``."""

from typing import Literal, TypeAlias, cast

StoreType: TypeAlias = Literal[
    "SEQUENCE_STORE",
    "REFERENCE_STORE",
]


# --- restJson1 ser/de ---
def serialize_json(value: StoreType) -> str:
    return value


def deserialize_json(data: str) -> StoreType:
    return cast(StoreType, data)
