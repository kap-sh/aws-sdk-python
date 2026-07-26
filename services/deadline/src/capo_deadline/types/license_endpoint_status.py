"""Generated from Smithy shape ``com.amazonaws.deadline#LicenseEndpointStatus``."""

from typing import Literal, TypeAlias, cast

LicenseEndpointStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "DELETE_IN_PROGRESS",
    "READY",
    "NOT_READY",
]


# --- restJson1 ser/de ---
def serialize_json(value: LicenseEndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> LicenseEndpointStatus:
    return cast(LicenseEndpointStatus, data)
