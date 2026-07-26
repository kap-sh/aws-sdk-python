"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ActorType``."""

from typing import Literal, TypeAlias, cast

ActorType: TypeAlias = Literal[
    "USER",
    "SYSTEM",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActorType) -> str:
    return value


def deserialize_json(data: str) -> ActorType:
    return cast(ActorType, data)
