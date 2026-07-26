"""Generated from Smithy shape ``com.amazonaws.entityresolution#StatementEffect``."""

from typing import Literal, TypeAlias, cast

StatementEffect: TypeAlias = Literal[
    "Allow",
    "Deny",
]


# --- restJson1 ser/de ---
def serialize_json(value: StatementEffect) -> str:
    return value


def deserialize_json(data: str) -> StatementEffect:
    return cast(StatementEffect, data)
