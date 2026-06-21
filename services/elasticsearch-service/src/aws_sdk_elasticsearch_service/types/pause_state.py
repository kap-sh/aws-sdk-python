"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PauseState``."""

from typing import Literal, TypeAlias, cast

PauseState: TypeAlias = Literal[
    "Active",
    "Completed",
    "Scheduled",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: PauseState) -> str:
    return value


def deserialize_json(data: str) -> PauseState:
    return cast(PauseState, data)
