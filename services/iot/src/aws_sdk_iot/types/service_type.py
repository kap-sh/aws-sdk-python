"""Generated from Smithy shape ``com.amazonaws.iot#ServiceType``."""

from typing import Literal, TypeAlias, cast

ServiceType: TypeAlias = Literal[
    "DATA",
    "CREDENTIAL_PROVIDER",
    "JOBS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceType) -> str:
    return value


def deserialize_json(data: str) -> ServiceType:
    return cast(ServiceType, data)
