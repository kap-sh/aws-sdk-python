"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#TargetStatus``."""

from typing import Literal, TypeAlias, cast

TargetStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "UNREACHABLE",
    "INACTIVE",
    "DEACTIVATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetStatus) -> str:
    return value


def deserialize_json(data: str) -> TargetStatus:
    return cast(TargetStatus, data)
