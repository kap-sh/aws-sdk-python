"""Generated from Smithy shape ``com.amazonaws.appsync#ConflictHandlerType``."""

from typing import Literal, TypeAlias, cast

ConflictHandlerType: TypeAlias = Literal[
    "OPTIMISTIC_CONCURRENCY",
    "LAMBDA",
    "AUTOMERGE",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictHandlerType) -> str:
    return value


def deserialize_json(data: str) -> ConflictHandlerType:
    return cast(ConflictHandlerType, data)
