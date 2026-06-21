"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexAlertState``."""

from typing import Literal, TypeAlias, cast

"""The possible states of a multiplex alert. SET - The alert is actively happening. CLEARED - The alert is no longer happening."""
MultiplexAlertState: TypeAlias = Literal[
    "SET",
    "CLEARED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexAlertState) -> str:
    return value


def deserialize_json(data: str) -> MultiplexAlertState:
    return cast(MultiplexAlertState, data)
