"""Generated from Smithy shape ``com.amazonaws.rdsdata#LongReturnType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds_data.errors import DeserializationError

LongReturnType: TypeAlias = Literal[
    "STRING",
    "LONG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "LONG",
    )
)


def serialize_json(value: LongReturnType) -> str:
    return value


def deserialize_json(data: str) -> LongReturnType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LongReturnType value: {data!r}")
    return cast(LongReturnType, data)
