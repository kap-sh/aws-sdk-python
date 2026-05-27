"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityDeletePropagationPolicy``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

CapabilityDeletePropagationPolicy: TypeAlias = Literal["RETAIN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RETAIN",))


def serialize_json(value: CapabilityDeletePropagationPolicy) -> str:
    return value


def deserialize_json(data: str) -> CapabilityDeletePropagationPolicy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CapabilityDeletePropagationPolicy value: {data!r}"
        )
    return cast(CapabilityDeletePropagationPolicy, data)
