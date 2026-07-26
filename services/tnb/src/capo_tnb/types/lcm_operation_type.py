"""Generated from Smithy shape ``com.amazonaws.tnb#LcmOperationType``."""

from typing import Literal, TypeAlias, cast

LcmOperationType: TypeAlias = Literal[
    "INSTANTIATE",
    "UPDATE",
    "TERMINATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: LcmOperationType) -> str:
    return value


def deserialize_json(data: str) -> LcmOperationType:
    return cast(LcmOperationType, data)
