"""Generated from Smithy shape ``com.amazonaws.securityhub#AdminStatus``."""

from typing import Literal, TypeAlias, cast

AdminStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdminStatus) -> str:
    return value


def deserialize_json(data: str) -> AdminStatus:
    return cast(AdminStatus, data)
