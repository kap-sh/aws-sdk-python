"""Generated from Smithy shape ``com.amazonaws.opensearch#ActionStatus``."""

from typing import Literal, TypeAlias, cast

ActionStatus: TypeAlias = Literal[
    "PENDING_UPDATE",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
    "NOT_ELIGIBLE",
    "ELIGIBLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionStatus) -> str:
    return value


def deserialize_json(data: str) -> ActionStatus:
    return cast(ActionStatus, data)
