"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyValueSource``."""

from typing import Literal, TypeAlias, cast

PolicyValueSource: TypeAlias = Literal[
    "SELF",
    "CROSS_ACCOUNT",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyValueSource) -> str:
    return value


def deserialize_json(data: str) -> PolicyValueSource:
    return cast(PolicyValueSource, data)
