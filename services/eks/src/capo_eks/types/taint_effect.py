"""Generated from Smithy shape ``com.amazonaws.eks#TaintEffect``."""

from typing import Literal, TypeAlias, cast

TaintEffect: TypeAlias = Literal[
    "NO_SCHEDULE",
    "NO_EXECUTE",
    "PREFER_NO_SCHEDULE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaintEffect) -> str:
    return value


def deserialize_json(data: str) -> TaintEffect:
    return cast(TaintEffect, data)
