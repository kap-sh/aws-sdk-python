"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentStatus``."""

from typing import Literal, TypeAlias, cast

ServiceEnvironmentStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "DELETED",
    "VALID",
    "INVALID",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEnvironmentStatus) -> str:
    return value


def deserialize_json(data: str) -> ServiceEnvironmentStatus:
    return cast(ServiceEnvironmentStatus, data)
