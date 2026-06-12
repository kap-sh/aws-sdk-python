"""Generated from Smithy shape ``com.amazonaws.artifact#NotificationSubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_artifact.errors import DeserializationError

NotificationSubscriptionStatus: TypeAlias = Literal[
    "SUBSCRIBED",
    "NOT_SUBSCRIBED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBSCRIBED",
        "NOT_SUBSCRIBED",
    )
)


def serialize_json(value: NotificationSubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> NotificationSubscriptionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NotificationSubscriptionStatus value: {data!r}"
        )
    return cast(NotificationSubscriptionStatus, data)
