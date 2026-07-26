"""Generated from Smithy shape ``com.amazonaws.qbusiness#RetrieverType``."""

from typing import Literal, TypeAlias, cast

RetrieverType: TypeAlias = Literal[
    "NATIVE_INDEX",
    "KENDRA_INDEX",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrieverType) -> str:
    return value


def deserialize_json(data: str) -> RetrieverType:
    return cast(RetrieverType, data)
