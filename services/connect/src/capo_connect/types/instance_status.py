"""Generated from Smithy shape ``com.amazonaws.connect#InstanceStatus``."""

from typing import Literal, TypeAlias, cast

InstanceStatus: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "ACTIVE",
    "CREATION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceStatus) -> str:
    return value


def deserialize_json(data: str) -> InstanceStatus:
    return cast(InstanceStatus, data)
