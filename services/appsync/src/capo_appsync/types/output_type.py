"""Generated from Smithy shape ``com.amazonaws.appsync#OutputType``."""

from typing import Literal, TypeAlias, cast

OutputType: TypeAlias = Literal[
    "SDL",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputType) -> str:
    return value


def deserialize_json(data: str) -> OutputType:
    return cast(OutputType, data)
