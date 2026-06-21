"""Generated from Smithy shape ``com.amazonaws.lakeformation#TransactionType``."""

from typing import Literal, TypeAlias, cast

TransactionType: TypeAlias = Literal[
    "READ_AND_WRITE",
    "READ_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: TransactionType) -> str:
    return value


def deserialize_json(data: str) -> TransactionType:
    return cast(TransactionType, data)
