"""Generated from Smithy shape ``com.amazonaws.inspector2#RuleSetCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

RuleSetCategory: TypeAlias = Literal[
    "SAST",
    "IAC",
    "SCA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAST",
        "IAC",
        "SCA",
    )
)


def serialize_json(value: RuleSetCategory) -> str:
    return value


def deserialize_json(data: str) -> RuleSetCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleSetCategory value: {data!r}")
    return cast(RuleSetCategory, data)
