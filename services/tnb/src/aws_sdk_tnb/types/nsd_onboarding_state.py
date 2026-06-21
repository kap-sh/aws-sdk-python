"""Generated from Smithy shape ``com.amazonaws.tnb#NsdOnboardingState``."""

from typing import Literal, TypeAlias, cast

NsdOnboardingState: TypeAlias = Literal[
    "CREATED",
    "ONBOARDED",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: NsdOnboardingState) -> str:
    return value


def deserialize_json(data: str) -> NsdOnboardingState:
    return cast(NsdOnboardingState, data)
