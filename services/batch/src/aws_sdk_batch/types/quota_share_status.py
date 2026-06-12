"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

QuotaShareStatus: TypeAlias = Literal[
    "CREATING",
    "VALID",
    "INVALID",
    "UPDATING",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "VALID",
        "INVALID",
        "UPDATING",
        "DELETING",
    )
)


def serialize_json(value: QuotaShareStatus) -> str:
    return value


def deserialize_json(data: str) -> QuotaShareStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuotaShareStatus value: {data!r}")
    return cast(QuotaShareStatus, data)
