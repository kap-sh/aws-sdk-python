"""Generated from Smithy shape ``com.amazonaws.eks#WarmPoolState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

WarmPoolState: TypeAlias = Literal[
    "STOPPED",
    "RUNNING",
    "HIBERNATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STOPPED",
        "RUNNING",
        "HIBERNATED",
    )
)


def serialize_json(value: WarmPoolState) -> str:
    return value


def deserialize_json(data: str) -> WarmPoolState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WarmPoolState value: {data!r}")
    return cast(WarmPoolState, data)
