"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencyCriticality``."""

from typing import Literal, TypeAlias, cast

DependencyCriticality: TypeAlias = Literal[
    "HARD",
    "SOFT",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyCriticality) -> str:
    return value


def deserialize_json(data: str) -> DependencyCriticality:
    return cast(DependencyCriticality, data)
