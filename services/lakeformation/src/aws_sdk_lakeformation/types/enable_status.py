"""Generated from Smithy shape ``com.amazonaws.lakeformation#EnableStatus``."""

from typing import Literal, TypeAlias, cast

EnableStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnableStatus) -> str:
    return value


def deserialize_json(data: str) -> EnableStatus:
    return cast(EnableStatus, data)
