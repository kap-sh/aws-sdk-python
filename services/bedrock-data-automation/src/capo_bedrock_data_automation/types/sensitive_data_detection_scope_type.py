"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#SensitiveDataDetectionScopeType``."""

from typing import Literal, TypeAlias, cast

"""Types of sensitive data detection scope"""
SensitiveDataDetectionScopeType: TypeAlias = Literal[
    "STANDARD",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDataDetectionScopeType) -> str:
    return value


def deserialize_json(data: str) -> SensitiveDataDetectionScopeType:
    return cast(SensitiveDataDetectionScopeType, data)
