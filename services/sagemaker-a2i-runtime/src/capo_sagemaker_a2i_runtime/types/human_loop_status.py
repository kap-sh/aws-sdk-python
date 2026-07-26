"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#HumanLoopStatus``."""

from typing import Literal, TypeAlias, cast

HumanLoopStatus: TypeAlias = Literal[
    "InProgress",
    "Failed",
    "Completed",
    "Stopped",
    "Stopping",
]


# --- restJson1 ser/de ---
def serialize_json(value: HumanLoopStatus) -> str:
    return value


def deserialize_json(data: str) -> HumanLoopStatus:
    return cast(HumanLoopStatus, data)
