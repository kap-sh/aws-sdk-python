"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareInSharePreemptionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

QuotaShareInSharePreemptionState: TypeAlias = Literal[
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


def serialize_json(value: QuotaShareInSharePreemptionState) -> str:
    return value


def deserialize_json(data: str) -> QuotaShareInSharePreemptionState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown QuotaShareInSharePreemptionState value: {data!r}"
        )
    return cast(QuotaShareInSharePreemptionState, data)
