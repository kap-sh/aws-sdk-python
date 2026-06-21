"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineDriftStatus``."""

from typing import Literal, TypeAlias, cast

EnabledBaselineDriftStatus: TypeAlias = Literal[
    "IN_SYNC",
    "DRIFTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineDriftStatus) -> str:
    return value


def deserialize_json(data: str) -> EnabledBaselineDriftStatus:
    return cast(EnabledBaselineDriftStatus, data)
