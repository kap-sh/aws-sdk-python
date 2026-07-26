"""Generated from Smithy shape ``com.amazonaws.qbusiness#RetrieverStatus``."""

from typing import Literal, TypeAlias, cast

RetrieverStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrieverStatus) -> str:
    return value


def deserialize_json(data: str) -> RetrieverStatus:
    return cast(RetrieverStatus, data)
