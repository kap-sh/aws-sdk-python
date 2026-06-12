"""Generated from Smithy shape ``com.amazonaws.deadline#RangeConstraint``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

RangeConstraint: TypeAlias = Literal[
    "CONTIGUOUS",
    "NONCONTIGUOUS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTIGUOUS",
        "NONCONTIGUOUS",
    )
)


def serialize_json(value: RangeConstraint) -> str:
    return value


def deserialize_json(data: str) -> RangeConstraint:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RangeConstraint value: {data!r}")
    return cast(RangeConstraint, data)
