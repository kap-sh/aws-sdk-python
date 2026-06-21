"""Generated from Smithy shape ``com.amazonaws.efs#ThroughputMode``."""

from typing import Literal, TypeAlias, cast

ThroughputMode: TypeAlias = Literal[
    "bursting",
    "provisioned",
    "elastic",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThroughputMode) -> str:
    return value


def deserialize_json(data: str) -> ThroughputMode:
    return cast(ThroughputMode, data)
