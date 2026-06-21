"""Generated from Smithy shape ``com.amazonaws.medialive#AccessibilityType``."""

from typing import Literal, TypeAlias, cast

"""Accessibility Type"""
AccessibilityType: TypeAlias = Literal[
    "DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES",
    "IMPLEMENTS_ACCESSIBILITY_FEATURES",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessibilityType) -> str:
    return value


def deserialize_json(data: str) -> AccessibilityType:
    return cast(AccessibilityType, data)
