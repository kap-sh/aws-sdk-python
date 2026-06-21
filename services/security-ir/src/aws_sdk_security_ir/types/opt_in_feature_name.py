"""Generated from Smithy shape ``com.amazonaws.securityir#OptInFeatureName``."""

from typing import Literal, TypeAlias, cast

OptInFeatureName: TypeAlias = Literal["Triage",]


# --- restJson1 ser/de ---
def serialize_json(value: OptInFeatureName) -> str:
    return value


def deserialize_json(data: str) -> OptInFeatureName:
    return cast(OptInFeatureName, data)
