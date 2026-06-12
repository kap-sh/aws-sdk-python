"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSourceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Used in SdiSource, DescribeNodeRequest, DescribeNodeResult"""
SdiSourceState: TypeAlias = Literal[
    "IDLE",
    "IN_USE",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IDLE",
        "IN_USE",
        "DELETED",
    )
)


def serialize_json(value: SdiSourceState) -> str:
    return value


def deserialize_json(data: str) -> SdiSourceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SdiSourceState value: {data!r}")
    return cast(SdiSourceState, data)
