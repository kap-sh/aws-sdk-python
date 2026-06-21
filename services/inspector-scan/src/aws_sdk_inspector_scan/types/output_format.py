"""Generated from Smithy shape ``com.amazonaws.inspectorscan#OutputFormat``."""

from typing import Literal, TypeAlias, cast

OutputFormat: TypeAlias = Literal[
    "CYCLONE_DX_1_5",
    "INSPECTOR",
    "INSPECTOR_ALT",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputFormat) -> str:
    return value


def deserialize_json(data: str) -> OutputFormat:
    return cast(OutputFormat, data)
