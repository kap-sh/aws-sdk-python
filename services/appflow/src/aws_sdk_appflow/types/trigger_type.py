"""Generated from Smithy shape ``com.amazonaws.appflow#TriggerType``."""

from typing import Literal, TypeAlias, cast

TriggerType: TypeAlias = Literal[
    "Scheduled",
    "Event",
    "OnDemand",
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerType) -> str:
    return value


def deserialize_json(data: str) -> TriggerType:
    return cast(TriggerType, data)
