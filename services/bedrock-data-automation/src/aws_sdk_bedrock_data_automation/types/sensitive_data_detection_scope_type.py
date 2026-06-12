"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#SensitiveDataDetectionScopeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Types of sensitive data detection scope"""
SensitiveDataDetectionScopeType: TypeAlias = Literal[
    "STANDARD",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "CUSTOM",
    )
)


def serialize_json(value: SensitiveDataDetectionScopeType) -> str:
    return value


def deserialize_json(data: str) -> SensitiveDataDetectionScopeType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SensitiveDataDetectionScopeType value: {data!r}"
        )
    return cast(SensitiveDataDetectionScopeType, data)
