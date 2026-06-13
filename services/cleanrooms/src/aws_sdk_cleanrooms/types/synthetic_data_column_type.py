"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SyntheticDataColumnType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

SyntheticDataColumnType: TypeAlias = Literal[
    "CATEGORICAL",
    "NUMERICAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CATEGORICAL",
        "NUMERICAL",
    )
)


def serialize_json(value: SyntheticDataColumnType) -> str:
    return value


def deserialize_json(data: str) -> SyntheticDataColumnType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SyntheticDataColumnType value: {data!r}")
    return cast(SyntheticDataColumnType, data)
