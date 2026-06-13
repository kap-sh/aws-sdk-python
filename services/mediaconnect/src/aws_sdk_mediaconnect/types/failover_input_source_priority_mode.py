"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverInputSourcePriorityMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

FailoverInputSourcePriorityMode: TypeAlias = Literal[
    "NO_PRIORITY",
    "PRIMARY_SECONDARY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_PRIORITY",
        "PRIMARY_SECONDARY",
    )
)


def serialize_json(value: FailoverInputSourcePriorityMode) -> str:
    return value


def deserialize_json(data: str) -> FailoverInputSourcePriorityMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FailoverInputSourcePriorityMode value: {data!r}"
        )
    return cast(FailoverInputSourcePriorityMode, data)
