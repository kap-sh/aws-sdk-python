"""Generated from Smithy shape ``com.amazonaws.securityhub#ControlStatus``."""

from typing import Literal, TypeAlias, cast

ControlStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlStatus) -> str:
    return value


def deserialize_json(data: str) -> ControlStatus:
    return cast(ControlStatus, data)
