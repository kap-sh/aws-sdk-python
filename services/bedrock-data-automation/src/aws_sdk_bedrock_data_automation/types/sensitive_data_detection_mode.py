"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#SensitiveDataDetectionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Mode for sensitive data detection"""
SensitiveDataDetectionMode: TypeAlias = Literal[
    "DETECTION",
    "DETECTION_AND_REDACTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DETECTION",
        "DETECTION_AND_REDACTION",
    )
)


def serialize_json(value: SensitiveDataDetectionMode) -> str:
    return value


def deserialize_json(data: str) -> SensitiveDataDetectionMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SensitiveDataDetectionMode value: {data!r}"
        )
    return cast(SensitiveDataDetectionMode, data)
