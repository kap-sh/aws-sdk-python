"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

CapabilityType: TypeAlias = Literal[
    "ACK",
    "KRO",
    "ARGOCD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACK",
        "KRO",
        "ARGOCD",
    )
)


def serialize_json(value: CapabilityType) -> str:
    return value


def deserialize_json(data: str) -> CapabilityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapabilityType value: {data!r}")
    return cast(CapabilityType, data)
