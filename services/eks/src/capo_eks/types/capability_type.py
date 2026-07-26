"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityType``."""

from typing import Literal, TypeAlias, cast

CapabilityType: TypeAlias = Literal[
    "ACK",
    "KRO",
    "ARGOCD",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityType) -> str:
    return value


def deserialize_json(data: str) -> CapabilityType:
    return cast(CapabilityType, data)
