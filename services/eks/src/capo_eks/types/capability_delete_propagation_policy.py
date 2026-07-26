"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityDeletePropagationPolicy``."""

from typing import Literal, TypeAlias, cast

CapabilityDeletePropagationPolicy: TypeAlias = Literal["RETAIN",]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityDeletePropagationPolicy) -> str:
    return value


def deserialize_json(data: str) -> CapabilityDeletePropagationPolicy:
    return cast(CapabilityDeletePropagationPolicy, data)
