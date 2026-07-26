"""Generated from Smithy shape ``com.amazonaws.lakeformation#TransactionStatusFilter``."""

from typing import Literal, TypeAlias, cast

TransactionStatusFilter: TypeAlias = Literal[
    "ALL",
    "COMPLETED",
    "ACTIVE",
    "COMMITTED",
    "ABORTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TransactionStatusFilter) -> str:
    return value


def deserialize_json(data: str) -> TransactionStatusFilter:
    return cast(TransactionStatusFilter, data)
