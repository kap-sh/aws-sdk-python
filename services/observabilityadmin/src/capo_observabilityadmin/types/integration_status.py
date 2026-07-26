"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#IntegrationStatus``."""

from typing import Literal, TypeAlias, cast

IntegrationStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationStatus) -> str:
    return value


def deserialize_json(data: str) -> IntegrationStatus:
    return cast(IntegrationStatus, data)
