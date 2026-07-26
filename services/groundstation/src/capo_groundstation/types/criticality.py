"""Generated from Smithy shape ``com.amazonaws.groundstation#Criticality``."""

from typing import Literal, TypeAlias, cast

Criticality: TypeAlias = Literal[
    "REQUIRED",
    "PREFERRED",
    "REMOVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Criticality) -> str:
    return value


def deserialize_json(data: str) -> Criticality:
    return cast(Criticality, data)
