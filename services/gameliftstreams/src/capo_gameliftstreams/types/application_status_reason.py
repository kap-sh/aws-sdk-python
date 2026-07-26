"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ApplicationStatusReason``."""

from typing import Literal, TypeAlias, cast

ApplicationStatusReason: TypeAlias = Literal[
    "internalError",
    "accessDenied",
    "sourceModified",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationStatusReason) -> str:
    return value


def deserialize_json(data: str) -> ApplicationStatusReason:
    return cast(ApplicationStatusReason, data)
