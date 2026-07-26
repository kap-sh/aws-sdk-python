"""Generated from Smithy shape ``com.amazonaws.qbusiness#OutputFormat``."""

from typing import Literal, TypeAlias, cast

OutputFormat: TypeAlias = Literal[
    "RAW",
    "EXTRACTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputFormat) -> str:
    return value


def deserialize_json(data: str) -> OutputFormat:
    return cast(OutputFormat, data)
