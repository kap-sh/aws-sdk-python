"""Generated from Smithy shape ``com.amazonaws.codeartifact#AllowUpstream``."""

from typing import Literal, TypeAlias, cast

AllowUpstream: TypeAlias = Literal[
    "ALLOW",
    "BLOCK",
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowUpstream) -> str:
    return value


def deserialize_json(data: str) -> AllowUpstream:
    return cast(AllowUpstream, data)
