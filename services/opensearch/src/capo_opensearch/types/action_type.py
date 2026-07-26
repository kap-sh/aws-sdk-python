"""Generated from Smithy shape ``com.amazonaws.opensearch#ActionType``."""

from typing import Literal, TypeAlias, cast

ActionType: TypeAlias = Literal[
    "SERVICE_SOFTWARE_UPDATE",
    "JVM_HEAP_SIZE_TUNING",
    "JVM_YOUNG_GEN_TUNING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionType) -> str:
    return value


def deserialize_json(data: str) -> ActionType:
    return cast(ActionType, data)
