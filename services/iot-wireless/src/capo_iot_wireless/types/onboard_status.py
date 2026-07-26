"""Generated from Smithy shape ``com.amazonaws.iotwireless#OnboardStatus``."""

from typing import Literal, TypeAlias, cast

OnboardStatus: TypeAlias = Literal[
    "INITIALIZED",
    "PENDING",
    "ONBOARDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OnboardStatus) -> str:
    return value


def deserialize_json(data: str) -> OnboardStatus:
    return cast(OnboardStatus, data)
