"""Generated from Smithy shape ``com.amazonaws.medialive#ClusterAlertState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The possible states of a cluster alert. SET - The alert is actively happening. CLEARED - The alert is no longer happening."""
ClusterAlertState: TypeAlias = Literal[
    "SET",
    "CLEARED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SET",
        "CLEARED",
    )
)


def serialize_json(value: ClusterAlertState) -> str:
    return value


def deserialize_json(data: str) -> ClusterAlertState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterAlertState value: {data!r}")
    return cast(ClusterAlertState, data)
