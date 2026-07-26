"""Generated from Smithy shape ``com.amazonaws.neptunedata#Parallelism``."""

from typing import Literal, TypeAlias, cast

Parallelism: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "OVERSUBSCRIBE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Parallelism) -> str:
    return value


def deserialize_json(data: str) -> Parallelism:
    return cast(Parallelism, data)
