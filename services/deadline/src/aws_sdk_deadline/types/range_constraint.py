"""Generated from Smithy shape ``com.amazonaws.deadline#RangeConstraint``."""

from typing import Literal, TypeAlias, cast

RangeConstraint: TypeAlias = Literal[
    "CONTIGUOUS",
    "NONCONTIGUOUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: RangeConstraint) -> str:
    return value


def deserialize_json(data: str) -> RangeConstraint:
    return cast(RangeConstraint, data)
