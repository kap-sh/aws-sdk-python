"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PortalType``."""

from typing import Literal, TypeAlias, cast

PortalType: TypeAlias = Literal[
    "SITEWISE_PORTAL_V1",
    "SITEWISE_PORTAL_V2",
]


# --- restJson1 ser/de ---
def serialize_json(value: PortalType) -> str:
    return value


def deserialize_json(data: str) -> PortalType:
    return cast(PortalType, data)
