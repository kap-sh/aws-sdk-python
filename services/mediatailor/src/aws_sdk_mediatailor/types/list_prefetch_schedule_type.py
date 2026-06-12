"""Generated from Smithy shape ``com.amazonaws.mediatailor#ListPrefetchScheduleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

ListPrefetchScheduleType: TypeAlias = Literal[
    "SINGLE",
    "RECURRING",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE",
        "RECURRING",
        "ALL",
    )
)


def serialize_json(value: ListPrefetchScheduleType) -> str:
    return value


def deserialize_json(data: str) -> ListPrefetchScheduleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListPrefetchScheduleType value: {data!r}")
    return cast(ListPrefetchScheduleType, data)
