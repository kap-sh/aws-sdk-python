"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

QuotaShareState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: QuotaShareState) -> str:
    return value


def deserialize_json(data: str) -> QuotaShareState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuotaShareState value: {data!r}")
    return cast(QuotaShareState, data)
