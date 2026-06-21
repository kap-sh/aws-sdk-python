"""Generated from Smithy shape ``com.amazonaws.iot#OutputFormat``."""

from typing import Literal, TypeAlias, cast

OutputFormat: TypeAlias = Literal[
    "JSON",
    "CBOR",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputFormat) -> str:
    return value


def deserialize_json(data: str) -> OutputFormat:
    return cast(OutputFormat, data)
