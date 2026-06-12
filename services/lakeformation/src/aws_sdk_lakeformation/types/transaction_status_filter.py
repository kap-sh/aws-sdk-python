"""Generated from Smithy shape ``com.amazonaws.lakeformation#TransactionStatusFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

TransactionStatusFilter: TypeAlias = Literal[
    "ALL",
    "COMPLETED",
    "ACTIVE",
    "COMMITTED",
    "ABORTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "COMPLETED",
        "ACTIVE",
        "COMMITTED",
        "ABORTED",
    )
)


def serialize_json(value: TransactionStatusFilter) -> str:
    return value


def deserialize_json(data: str) -> TransactionStatusFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransactionStatusFilter value: {data!r}")
    return cast(TransactionStatusFilter, data)
