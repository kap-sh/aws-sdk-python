"""Generated from Smithy shape ``com.amazonaws.finspace#RuleAction``."""

from typing import Literal, TypeAlias, cast

RuleAction: TypeAlias = Literal[
    "allow",
    "deny",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleAction) -> str:
    return value


def deserialize_json(data: str) -> RuleAction:
    return cast(RuleAction, data)
