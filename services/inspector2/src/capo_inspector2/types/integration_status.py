"""Generated from Smithy shape ``com.amazonaws.inspector2#IntegrationStatus``."""

from typing import Literal, TypeAlias, cast

IntegrationStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "ACTIVE",
    "INACTIVE",
    "DISABLING",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationStatus) -> str:
    return value


def deserialize_json(data: str) -> IntegrationStatus:
    return cast(IntegrationStatus, data)
