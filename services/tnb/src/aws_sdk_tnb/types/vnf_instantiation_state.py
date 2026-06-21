"""Generated from Smithy shape ``com.amazonaws.tnb#VnfInstantiationState``."""

from typing import Literal, TypeAlias, cast

VnfInstantiationState: TypeAlias = Literal[
    "INSTANTIATED",
    "NOT_INSTANTIATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VnfInstantiationState) -> str:
    return value


def deserialize_json(data: str) -> VnfInstantiationState:
    return cast(VnfInstantiationState, data)
