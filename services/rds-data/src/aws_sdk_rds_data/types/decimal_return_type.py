"""Generated from Smithy shape ``com.amazonaws.rdsdata#DecimalReturnType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds_data.errors import DeserializationError

DecimalReturnType: TypeAlias = Literal[
    "STRING",
    "DOUBLE_OR_LONG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "DOUBLE_OR_LONG",
    )
)


def serialize_json(value: DecimalReturnType) -> str:
    return value


def deserialize_json(data: str) -> DecimalReturnType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DecimalReturnType value: {data!r}")
    return cast(DecimalReturnType, data)
