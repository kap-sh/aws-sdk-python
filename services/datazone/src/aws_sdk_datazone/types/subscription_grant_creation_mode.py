"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionGrantCreationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

SubscriptionGrantCreationMode: TypeAlias = Literal[
    "AUTOMATIC",
    "MANUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "MANUAL",
    )
)


def serialize_json(value: SubscriptionGrantCreationMode) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionGrantCreationMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SubscriptionGrantCreationMode value: {data!r}"
        )
    return cast(SubscriptionGrantCreationMode, data)
