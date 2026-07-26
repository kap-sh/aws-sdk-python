"""Generated from Smithy shape ``com.amazonaws.appsync#InvokeType``."""

from typing import Literal, TypeAlias, cast

InvokeType: TypeAlias = Literal[
    "REQUEST_RESPONSE",
    "EVENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvokeType) -> str:
    return value


def deserialize_json(data: str) -> InvokeType:
    return cast(InvokeType, data)
