"""Generated from Smithy shape ``com.amazonaws.mpa#PolicyType``."""

from typing import Literal, TypeAlias, cast

PolicyType: TypeAlias = Literal[
    "AWS_MANAGED",
    "AWS_RAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyType) -> str:
    return value


def deserialize_json(data: str) -> PolicyType:
    return cast(PolicyType, data)
