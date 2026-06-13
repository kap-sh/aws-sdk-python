"""Generated from Smithy shape ``com.amazonaws.bedrock#SelectiveGuardingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

SelectiveGuardingMode: TypeAlias = Literal[
    "SELECTIVE",
    "COMPREHENSIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELECTIVE",
        "COMPREHENSIVE",
    )
)


def serialize_json(value: SelectiveGuardingMode) -> str:
    return value


def deserialize_json(data: str) -> SelectiveGuardingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelectiveGuardingMode value: {data!r}")
    return cast(SelectiveGuardingMode, data)
