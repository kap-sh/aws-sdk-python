"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AdditionalResourceType``."""

from typing import Literal, TypeAlias, cast

AdditionalResourceType: TypeAlias = Literal[
    "HELPFUL_RESOURCE",
    "IMPROVEMENT_PLAN",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalResourceType) -> str:
    return value


def deserialize_json(data: str) -> AdditionalResourceType:
    return cast(AdditionalResourceType, data)
