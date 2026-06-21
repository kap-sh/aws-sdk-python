"""Generated from Smithy shape ``com.amazonaws.securityir#ResolverType``."""

from typing import Literal, TypeAlias, cast

ResolverType: TypeAlias = Literal[
    "AWS",
    "Self",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResolverType) -> str:
    return value


def deserialize_json(data: str) -> ResolverType:
    return cast(ResolverType, data)
