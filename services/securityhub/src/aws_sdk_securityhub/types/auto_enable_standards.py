"""Generated from Smithy shape ``com.amazonaws.securityhub#AutoEnableStandards``."""

from typing import Literal, TypeAlias, cast

AutoEnableStandards: TypeAlias = Literal[
    "NONE",
    "DEFAULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoEnableStandards) -> str:
    return value


def deserialize_json(data: str) -> AutoEnableStandards:
    return cast(AutoEnableStandards, data)
