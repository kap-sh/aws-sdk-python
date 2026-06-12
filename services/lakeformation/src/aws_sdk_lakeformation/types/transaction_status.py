"""Generated from Smithy shape ``com.amazonaws.lakeformation#TransactionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

TransactionStatus: TypeAlias = Literal[
    "ACTIVE",
    "COMMITTED",
    "ABORTED",
    "COMMIT_IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "COMMITTED",
        "ABORTED",
        "COMMIT_IN_PROGRESS",
    )
)


def serialize_json(value: TransactionStatus) -> str:
    return value


def deserialize_json(data: str) -> TransactionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransactionStatus value: {data!r}")
    return cast(TransactionStatus, data)
