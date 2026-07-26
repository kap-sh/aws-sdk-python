"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ResolutionStrategy``."""

from typing import Literal, TypeAlias, cast

ResolutionStrategy: TypeAlias = Literal[
    "OPTIMISTIC_CONCURRENCY",
    "LAMBDA",
    "AUTOMERGE",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResolutionStrategy) -> str:
    return value


def deserialize_json(data: str) -> ResolutionStrategy:
    return cast(ResolutionStrategy, data)
