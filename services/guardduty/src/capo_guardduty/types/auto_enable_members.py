"""Generated from Smithy shape ``com.amazonaws.guardduty#AutoEnableMembers``."""

from typing import Literal, TypeAlias, cast

AutoEnableMembers: TypeAlias = Literal[
    "NEW",
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoEnableMembers) -> str:
    return value


def deserialize_json(data: str) -> AutoEnableMembers:
    return cast(AutoEnableMembers, data)
