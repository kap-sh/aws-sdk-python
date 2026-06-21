"""Generated from Smithy shape ``com.amazonaws.workspacesweb#LogFileFormat``."""

from typing import Literal, TypeAlias, cast

LogFileFormat: TypeAlias = Literal[
    "JSONLines",
    "Json",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogFileFormat) -> str:
    return value


def deserialize_json(data: str) -> LogFileFormat:
    return cast(LogFileFormat, data)
