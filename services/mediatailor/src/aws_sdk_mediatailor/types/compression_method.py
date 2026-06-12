"""Generated from Smithy shape ``com.amazonaws.mediatailor#CompressionMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

CompressionMethod: TypeAlias = Literal[
    "NONE",
    "GZIP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "GZIP",
    )
)


def serialize_json(value: CompressionMethod) -> str:
    return value


def deserialize_json(data: str) -> CompressionMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompressionMethod value: {data!r}")
    return cast(CompressionMethod, data)
