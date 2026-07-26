"""Generated from Smithy shape ``com.amazonaws.inspector2#RuleSetCategory``."""

from typing import Literal, TypeAlias, cast

RuleSetCategory: TypeAlias = Literal[
    "SAST",
    "IAC",
    "SCA",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleSetCategory) -> str:
    return value


def deserialize_json(data: str) -> RuleSetCategory:
    return cast(RuleSetCategory, data)
