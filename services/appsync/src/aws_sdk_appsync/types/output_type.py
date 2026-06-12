"""Generated from Smithy shape ``com.amazonaws.appsync#OutputType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

OutputType: TypeAlias = Literal[
    "SDL",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SDL",
        "JSON",
    )
)


def serialize_json(value: OutputType) -> str:
    return value


def deserialize_json(data: str) -> OutputType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputType value: {data!r}")
    return cast(OutputType, data)
