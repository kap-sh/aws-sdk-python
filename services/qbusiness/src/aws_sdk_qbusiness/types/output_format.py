"""Generated from Smithy shape ``com.amazonaws.qbusiness#OutputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

OutputFormat: TypeAlias = Literal[
    "RAW",
    "EXTRACTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RAW",
        "EXTRACTED",
    )
)


def serialize_json(value: OutputFormat) -> str:
    return value


def deserialize_json(data: str) -> OutputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputFormat value: {data!r}")
    return cast(OutputFormat, data)
