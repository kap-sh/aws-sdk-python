"""Generated from Smithy shape ``com.amazonaws.qbusiness#OrchestrationControl``."""

from typing import Literal, TypeAlias, cast

OrchestrationControl: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrchestrationControl) -> str:
    return value


def deserialize_json(data: str) -> OrchestrationControl:
    return cast(OrchestrationControl, data)
