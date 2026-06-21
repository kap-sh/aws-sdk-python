"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSourceState``."""

from typing import Literal, TypeAlias, cast

"""Used in SdiSource, DescribeNodeRequest, DescribeNodeResult"""
SdiSourceState: TypeAlias = Literal[
    "IDLE",
    "IN_USE",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SdiSourceState) -> str:
    return value


def deserialize_json(data: str) -> SdiSourceState:
    return cast(SdiSourceState, data)
