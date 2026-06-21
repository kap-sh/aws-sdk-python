"""Generated from Smithy shape ``com.amazonaws.medialive#SignalMapStatus``."""

from typing import Literal, TypeAlias, cast

"""A signal map's current status which is dependent on its lifecycle actions or associated jobs."""
SignalMapStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_REVERTED",
    "UPDATE_FAILED",
    "READY",
    "NOT_READY",
]


# --- restJson1 ser/de ---
def serialize_json(value: SignalMapStatus) -> str:
    return value


def deserialize_json(data: str) -> SignalMapStatus:
    return cast(SignalMapStatus, data)
