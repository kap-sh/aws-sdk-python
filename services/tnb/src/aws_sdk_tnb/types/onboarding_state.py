"""Generated from Smithy shape ``com.amazonaws.tnb#OnboardingState``."""

from typing import Literal, TypeAlias, cast

OnboardingState: TypeAlias = Literal[
    "CREATED",
    "ONBOARDED",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: OnboardingState) -> str:
    return value


def deserialize_json(data: str) -> OnboardingState:
    return cast(OnboardingState, data)
