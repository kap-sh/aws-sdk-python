"""Generated from Smithy shape ``com.amazonaws.iot#TopicRuleDestinationStatus``."""

from typing import Literal, TypeAlias, cast

TopicRuleDestinationStatus: TypeAlias = Literal[
    "ENABLED",
    "IN_PROGRESS",
    "DISABLED",
    "ERROR",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicRuleDestinationStatus) -> str:
    return value


def deserialize_json(data: str) -> TopicRuleDestinationStatus:
    return cast(TopicRuleDestinationStatus, data)
