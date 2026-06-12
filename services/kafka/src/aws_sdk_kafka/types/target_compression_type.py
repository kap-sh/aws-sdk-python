"""Generated from Smithy shape ``com.amazonaws.kafka#TargetCompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The type of compression to use producing records to the target cluster.</p>"""
TargetCompressionType: TypeAlias = Literal[
    "NONE",
    "GZIP",
    "SNAPPY",
    "LZ4",
    "ZSTD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "GZIP",
        "SNAPPY",
        "LZ4",
        "ZSTD",
    )
)


def serialize_json(value: TargetCompressionType) -> str:
    return value


def deserialize_json(data: str) -> TargetCompressionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetCompressionType value: {data!r}")
    return cast(TargetCompressionType, data)
