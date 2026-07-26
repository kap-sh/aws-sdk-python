"""Generated from Smithy shape ``com.amazonaws.medialive#ClusterAlertState``."""

from typing import Literal, TypeAlias, cast

"""The possible states of a cluster alert. SET - The alert is actively happening. CLEARED - The alert is no longer happening."""
ClusterAlertState: TypeAlias = Literal[
    "SET",
    "CLEARED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterAlertState) -> str:
    return value


def deserialize_json(data: str) -> ClusterAlertState:
    return cast(ClusterAlertState, data)
