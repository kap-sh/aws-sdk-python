"""Generated from Smithy shape ``com.amazonaws.iotwireless#OnboardStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

OnboardStatus: TypeAlias = Literal[
    "INITIALIZED",
    "PENDING",
    "ONBOARDED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZED",
        "PENDING",
        "ONBOARDED",
        "FAILED",
    )
)


def serialize_json(value: OnboardStatus) -> str:
    return value


def deserialize_json(data: str) -> OnboardStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OnboardStatus value: {data!r}")
    return cast(OnboardStatus, data)
