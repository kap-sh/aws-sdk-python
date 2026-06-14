"""Generated from Smithy shape ``com.amazonaws.datazone#RuleScopeSelectionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

RuleScopeSelectionMode: TypeAlias = Literal[
    "ALL",
    "SPECIFIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "SPECIFIC",
    )
)


def serialize_json(value: RuleScopeSelectionMode) -> str:
    return value


def deserialize_json(data: str) -> RuleScopeSelectionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleScopeSelectionMode value: {data!r}")
    return cast(RuleScopeSelectionMode, data)
