"""Generated from Smithy shape ``com.amazonaws.lakeformation#TransactionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

TransactionType: TypeAlias = Literal[
    "READ_AND_WRITE",
    "READ_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ_AND_WRITE",
        "READ_ONLY",
    )
)


def serialize_json(value: TransactionType) -> str:
    return value


def deserialize_json(data: str) -> TransactionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransactionType value: {data!r}")
    return cast(TransactionType, data)
