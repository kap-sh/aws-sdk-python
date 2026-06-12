"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareIdleResourceAssignmentStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

QuotaShareIdleResourceAssignmentStrategy: TypeAlias = Literal["FIFO",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FIFO",))


def serialize_json(value: QuotaShareIdleResourceAssignmentStrategy) -> str:
    return value


def deserialize_json(data: str) -> QuotaShareIdleResourceAssignmentStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown QuotaShareIdleResourceAssignmentStrategy value: {data!r}"
        )
    return cast(QuotaShareIdleResourceAssignmentStrategy, data)
