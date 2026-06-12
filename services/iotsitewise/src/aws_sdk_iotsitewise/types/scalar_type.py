"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ScalarType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ScalarType: TypeAlias = Literal[
    "BOOLEAN",
    "INT",
    "DOUBLE",
    "TIMESTAMP",
    "STRING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BOOLEAN",
        "INT",
        "DOUBLE",
        "TIMESTAMP",
        "STRING",
    )
)


def serialize_json(value: ScalarType) -> str:
    return value


def deserialize_json(data: str) -> ScalarType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalarType value: {data!r}")
    return cast(ScalarType, data)
