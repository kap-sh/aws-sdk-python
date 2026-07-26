"""Generated from Smithy shape ``com.amazonaws.ssmsap#ApplicationDiscoveryStatus``."""

from typing import Literal, TypeAlias, cast

ApplicationDiscoveryStatus: TypeAlias = Literal[
    "SUCCESS",
    "REGISTRATION_FAILED",
    "REFRESH_FAILED",
    "REGISTERING",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationDiscoveryStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationDiscoveryStatus:
    return cast(ApplicationDiscoveryStatus, data)
