"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssertionSource``."""

from typing import Literal, TypeAlias, cast

AssertionSource: TypeAlias = Literal[
    "AI_GENERATED",
    "USER",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssertionSource) -> str:
    return value


def deserialize_json(data: str) -> AssertionSource:
    return cast(AssertionSource, data)
