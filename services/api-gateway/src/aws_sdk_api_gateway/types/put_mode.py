"""Generated from Smithy shape ``com.amazonaws.apigateway#PutMode``."""

from typing import Literal, TypeAlias, cast

PutMode: TypeAlias = Literal[
    "merge",
    "overwrite",
]


# --- restJson1 ser/de ---
def serialize_json(value: PutMode) -> str:
    return value


def deserialize_json(data: str) -> PutMode:
    return cast(PutMode, data)
