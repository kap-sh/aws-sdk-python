"""Generated from Smithy shape ``com.amazonaws.tnb#NsState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: NsState) -> str:
    return value


def deserialize_json(data: str) -> NsState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NsState value: {data!r}")
    return cast(NsState, data)
