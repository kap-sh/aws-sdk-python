"""Generated from Smithy shape ``com.amazonaws.iot#TopicRuleDestinationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

TopicRuleDestinationStatus: TypeAlias = Literal[
    "ENABLED",
    "IN_PROGRESS",
    "DISABLED",
    "ERROR",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "IN_PROGRESS",
        "DISABLED",
        "ERROR",
        "DELETING",
    )
)


def serialize_json(value: TopicRuleDestinationStatus) -> str:
    return value


def deserialize_json(data: str) -> TopicRuleDestinationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TopicRuleDestinationStatus value: {data!r}"
        )
    return cast(TopicRuleDestinationStatus, data)
