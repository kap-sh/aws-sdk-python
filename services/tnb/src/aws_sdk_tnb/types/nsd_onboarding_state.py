"""Generated from Smithy shape ``com.amazonaws.tnb#NsdOnboardingState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

NsdOnboardingState: TypeAlias = Literal[
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


def serialize_json(value: NsdOnboardingState) -> str:
    return value


def deserialize_json(data: str) -> NsdOnboardingState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NsdOnboardingState value: {data!r}")
    return cast(NsdOnboardingState, data)
