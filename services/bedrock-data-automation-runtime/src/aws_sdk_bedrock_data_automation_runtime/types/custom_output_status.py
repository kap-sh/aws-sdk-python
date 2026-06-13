"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#CustomOutputStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError

"""Custom output status enum"""
CustomOutputStatus: TypeAlias = Literal[
    "MATCH",
    "NO_MATCH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MATCH",
        "NO_MATCH",
    )
)


def serialize_aws_json_1_1(value: CustomOutputStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomOutputStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomOutputStatus value: {data!r}")
    return cast(CustomOutputStatus, data)
