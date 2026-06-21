"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#SensitiveDataDetectionMode``."""

from typing import Literal, TypeAlias, cast

"""Mode for sensitive data detection"""
SensitiveDataDetectionMode: TypeAlias = Literal[
    "DETECTION",
    "DETECTION_AND_REDACTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDataDetectionMode) -> str:
    return value


def deserialize_json(data: str) -> SensitiveDataDetectionMode:
    return cast(SensitiveDataDetectionMode, data)
