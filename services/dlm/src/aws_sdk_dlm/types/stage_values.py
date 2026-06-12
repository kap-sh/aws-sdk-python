"""Generated from Smithy shape ``com.amazonaws.dlm#StageValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

StageValues: TypeAlias = Literal[
    "PRE",
    "POST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRE",
        "POST",
    )
)


def serialize_json(value: StageValues) -> str:
    return value


def deserialize_json(data: str) -> StageValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StageValues value: {data!r}")
    return cast(StageValues, data)
