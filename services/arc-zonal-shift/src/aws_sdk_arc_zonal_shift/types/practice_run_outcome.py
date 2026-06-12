"""Generated from Smithy shape ``com.amazonaws.arczonalshift#PracticeRunOutcome``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_zonal_shift.errors import DeserializationError

PracticeRunOutcome: TypeAlias = Literal[
    "FAILED",
    "INTERRUPTED",
    "PENDING",
    "SUCCEEDED",
    "CAPACITY_CHECK_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "INTERRUPTED",
        "PENDING",
        "SUCCEEDED",
        "CAPACITY_CHECK_FAILED",
    )
)


def serialize_json(value: PracticeRunOutcome) -> str:
    return value


def deserialize_json(data: str) -> PracticeRunOutcome:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PracticeRunOutcome value: {data!r}")
    return cast(PracticeRunOutcome, data)
