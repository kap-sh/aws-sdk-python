"""Generated from Smithy shape ``com.amazonaws.quicksight#ServiceType``."""

from typing import Literal, TypeAlias, cast

ServiceType: TypeAlias = Literal[
    "REDSHIFT",
    "QBUSINESS",
    "ATHENA",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceType) -> str:
    return value


def deserialize_json(data: str) -> ServiceType:
    return cast(ServiceType, data)
