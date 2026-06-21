"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalyStatus``."""

from typing import Literal, TypeAlias, cast

AnomalyStatus: TypeAlias = Literal[
    "ONGOING",
    "CLOSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyStatus) -> str:
    return value


def deserialize_json(data: str) -> AnomalyStatus:
    return cast(AnomalyStatus, data)
