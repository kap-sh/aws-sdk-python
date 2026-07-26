"""Generated from Smithy shape ``com.amazonaws.entityresolution#ResolutionType``."""

from typing import Literal, TypeAlias, cast

ResolutionType: TypeAlias = Literal[
    "RULE_MATCHING",
    "ML_MATCHING",
    "PROVIDER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResolutionType) -> str:
    return value


def deserialize_json(data: str) -> ResolutionType:
    return cast(ResolutionType, data)
