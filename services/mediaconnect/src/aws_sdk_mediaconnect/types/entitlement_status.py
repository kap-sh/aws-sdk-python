"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EntitlementStatus``."""

from typing import Literal, TypeAlias, cast

EntitlementStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EntitlementStatus) -> str:
    return value


def deserialize_json(data: str) -> EntitlementStatus:
    return cast(EntitlementStatus, data)
