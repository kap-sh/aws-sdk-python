"""Generated from Smithy shape ``com.amazonaws.medialive#AccessibilityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Accessibility Type"""
AccessibilityType: TypeAlias = Literal[
    "DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES",
    "IMPLEMENTS_ACCESSIBILITY_FEATURES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES",
        "IMPLEMENTS_ACCESSIBILITY_FEATURES",
    )
)


def serialize_json(value: AccessibilityType) -> str:
    return value


def deserialize_json(data: str) -> AccessibilityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessibilityType value: {data!r}")
    return cast(AccessibilityType, data)
