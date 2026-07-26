"""Generated from Smithy shape ``com.amazonaws.iot#DomainType``."""

from typing import Literal, TypeAlias, cast

DomainType: TypeAlias = Literal[
    "ENDPOINT",
    "AWS_MANAGED",
    "CUSTOMER_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainType) -> str:
    return value


def deserialize_json(data: str) -> DomainType:
    return cast(DomainType, data)
