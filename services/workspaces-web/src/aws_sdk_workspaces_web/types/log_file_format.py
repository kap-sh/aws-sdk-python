"""Generated from Smithy shape ``com.amazonaws.workspacesweb#LogFileFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_web.errors import DeserializationError

LogFileFormat: TypeAlias = Literal[
    "JSONLines",
    "Json",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSONLines",
        "Json",
    )
)


def serialize_json(value: LogFileFormat) -> str:
    return value


def deserialize_json(data: str) -> LogFileFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogFileFormat value: {data!r}")
    return cast(LogFileFormat, data)
