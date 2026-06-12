"""Generated from Smithy shape ``com.amazonaws.mediatailor#PrefetchScheduleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

PrefetchScheduleType: TypeAlias = Literal[
    "SINGLE",
    "RECURRING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE",
        "RECURRING",
    )
)


def serialize_json(value: PrefetchScheduleType) -> str:
    return value


def deserialize_json(data: str) -> PrefetchScheduleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrefetchScheduleType value: {data!r}")
    return cast(PrefetchScheduleType, data)
