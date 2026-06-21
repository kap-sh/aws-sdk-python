"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionGrantCreationMode``."""

from typing import Literal, TypeAlias, cast

SubscriptionGrantCreationMode: TypeAlias = Literal[
    "AUTOMATIC",
    "MANUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionGrantCreationMode) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionGrantCreationMode:
    return cast(SubscriptionGrantCreationMode, data)
