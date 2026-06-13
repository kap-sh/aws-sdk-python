"""Generated from Smithy shape ``com.amazonaws.quicksight#LineInterpolation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

LineInterpolation: TypeAlias = Literal[
    "LINEAR",
    "SMOOTH",
    "STEPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINEAR",
        "SMOOTH",
        "STEPPED",
    )
)


def serialize_json(value: LineInterpolation) -> str:
    return value


def deserialize_json(data: str) -> LineInterpolation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LineInterpolation value: {data!r}")
    return cast(LineInterpolation, data)
