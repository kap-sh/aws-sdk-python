"""Generated from Smithy shape ``com.amazonaws.fis#SafetyLeverStatusInput``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fis.errors import DeserializationError

SafetyLeverStatusInput: TypeAlias = Literal[
    "disengaged",
    "engaged",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disengaged",
        "engaged",
    )
)


def serialize_json(value: SafetyLeverStatusInput) -> str:
    return value


def deserialize_json(data: str) -> SafetyLeverStatusInput:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SafetyLeverStatusInput value: {data!r}")
    return cast(SafetyLeverStatusInput, data)
