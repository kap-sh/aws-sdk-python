"""Generated from Smithy shape ``com.amazonaws.tnb#OnboardingState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

OnboardingState: TypeAlias = Literal[
    "CREATED",
    "ONBOARDED",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "ONBOARDED",
        "ERROR",
    )
)


def serialize_json(value: OnboardingState) -> str:
    return value


def deserialize_json(data: str) -> OnboardingState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OnboardingState value: {data!r}")
    return cast(OnboardingState, data)
