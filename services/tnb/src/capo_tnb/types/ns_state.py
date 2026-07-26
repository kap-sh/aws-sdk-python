"""Generated from Smithy shape ``com.amazonaws.tnb#NsState``."""

from typing import Literal, TypeAlias, cast

NsState: TypeAlias = Literal[
    "INSTANTIATED",
    "NOT_INSTANTIATED",
    "UPDATED",
    "IMPAIRED",
    "UPDATE_FAILED",
    "STOPPED",
    "DELETED",
    "INSTANTIATE_IN_PROGRESS",
    "INTENT_TO_UPDATE_IN_PROGRESS",
    "UPDATE_IN_PROGRESS",
    "TERMINATE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: NsState) -> str:
    return value


def deserialize_json(data: str) -> NsState:
    return cast(NsState, data)
