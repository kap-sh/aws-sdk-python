"""Generated from Smithy shape ``com.amazonaws.clouddirectory#RequiredAttributeBehavior``."""

from typing import Literal, TypeAlias, cast

RequiredAttributeBehavior: TypeAlias = Literal[
    "REQUIRED_ALWAYS",
    "NOT_REQUIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RequiredAttributeBehavior) -> str:
    return value


def deserialize_json(data: str) -> RequiredAttributeBehavior:
    return cast(RequiredAttributeBehavior, data)
