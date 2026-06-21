"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalyType``."""

from typing import Literal, TypeAlias, cast

AnomalyType: TypeAlias = Literal[
    "CAUSAL",
    "CONTEXTUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyType) -> str:
    return value


def deserialize_json(data: str) -> AnomalyType:
    return cast(AnomalyType, data)
