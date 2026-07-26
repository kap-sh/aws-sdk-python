"""Generated from Smithy shape ``com.amazonaws.datazone#RejectRuleBehavior``."""

from typing import Literal, TypeAlias, cast

RejectRuleBehavior: TypeAlias = Literal[
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RejectRuleBehavior) -> str:
    return value


def deserialize_json(data: str) -> RejectRuleBehavior:
    return cast(RejectRuleBehavior, data)
