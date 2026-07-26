"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptRuleBehavior``."""

from typing import Literal, TypeAlias, cast

AcceptRuleBehavior: TypeAlias = Literal[
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AcceptRuleBehavior) -> str:
    return value


def deserialize_json(data: str) -> AcceptRuleBehavior:
    return cast(AcceptRuleBehavior, data)
