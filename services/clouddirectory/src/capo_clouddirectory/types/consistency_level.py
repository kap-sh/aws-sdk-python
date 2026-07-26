"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ConsistencyLevel``."""

from typing import Literal, TypeAlias, cast

ConsistencyLevel: TypeAlias = Literal[
    "SERIALIZABLE",
    "EVENTUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConsistencyLevel) -> str:
    return value


def deserialize_json(data: str) -> ConsistencyLevel:
    return cast(ConsistencyLevel, data)
