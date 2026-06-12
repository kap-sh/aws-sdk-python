"""Generated from Smithy shape ``com.amazonaws.connectparticipant#SortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connectparticipant.errors import DeserializationError

SortKey: TypeAlias = Literal[
    "DESCENDING",
    "ASCENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DESCENDING",
        "ASCENDING",
    )
)


def serialize_json(value: SortKey) -> str:
    return value


def deserialize_json(data: str) -> SortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortKey value: {data!r}")
    return cast(SortKey, data)
