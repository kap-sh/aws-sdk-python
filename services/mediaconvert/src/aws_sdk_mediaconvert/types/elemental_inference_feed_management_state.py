"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ElementalInferenceFeedManagementState``."""

from typing import Literal, TypeAlias, cast

"""Elemental Inference Feed management state."""
ElementalInferenceFeedManagementState: TypeAlias = Literal[
    "CREATED",
    "ASSOCIATED",
    "PENDING_DELETION",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ElementalInferenceFeedManagementState) -> str:
    return value


def deserialize_json(data: str) -> ElementalInferenceFeedManagementState:
    return cast(ElementalInferenceFeedManagementState, data)
