"""Generated from Smithy shape ``com.amazonaws.connect#Grouping``."""

from typing import Literal, TypeAlias, cast

Grouping: TypeAlias = Literal[
    "QUEUE",
    "CHANNEL",
    "ROUTING_PROFILE",
    "ROUTING_STEP_EXPRESSION",
    "AGENT_STATUS",
    "SUBTYPE",
    "VALIDATION_TEST_TYPE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Grouping) -> str:
    return value


def deserialize_json(data: str) -> Grouping:
    return cast(Grouping, data)
