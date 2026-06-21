"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ServiceTierType``."""

from typing import Literal, TypeAlias, cast

ServiceTierType: TypeAlias = Literal[
    "priority",
    "default",
    "flex",
    "reserved",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceTierType) -> str:
    return value


def deserialize_json(data: str) -> ServiceTierType:
    return cast(ServiceTierType, data)
