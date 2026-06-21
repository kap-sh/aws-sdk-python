"""Generated from Smithy shape ``com.amazonaws.appsync#ResolverKind``."""

from typing import Literal, TypeAlias, cast

ResolverKind: TypeAlias = Literal[
    "UNIT",
    "PIPELINE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResolverKind) -> str:
    return value


def deserialize_json(data: str) -> ResolverKind:
    return cast(ResolverKind, data)
