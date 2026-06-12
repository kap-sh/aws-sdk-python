"""Generated from Smithy shape ``com.amazonaws.iot#OutputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

OutputFormat: TypeAlias = Literal[
    "JSON",
    "CBOR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "CBOR",
    )
)


def serialize_json(value: OutputFormat) -> str:
    return value


def deserialize_json(data: str) -> OutputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputFormat value: {data!r}")
    return cast(OutputFormat, data)
