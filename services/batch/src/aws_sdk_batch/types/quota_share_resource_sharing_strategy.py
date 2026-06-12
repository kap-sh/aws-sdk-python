"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareResourceSharingStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

QuotaShareResourceSharingStrategy: TypeAlias = Literal[
    "RESERVE",
    "LEND",
    "LEND_AND_BORROW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESERVE",
        "LEND",
        "LEND_AND_BORROW",
    )
)


def serialize_json(value: QuotaShareResourceSharingStrategy) -> str:
    return value


def deserialize_json(data: str) -> QuotaShareResourceSharingStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown QuotaShareResourceSharingStrategy value: {data!r}"
        )
    return cast(QuotaShareResourceSharingStrategy, data)
