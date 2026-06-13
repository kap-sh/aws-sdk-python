"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#DataAutomationStage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError

"""Data automation stage."""
DataAutomationStage: TypeAlias = Literal[
    "LIVE",
    "DEVELOPMENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LIVE",
        "DEVELOPMENT",
    )
)


def serialize_aws_json_1_1(value: DataAutomationStage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataAutomationStage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataAutomationStage value: {data!r}")
    return cast(DataAutomationStage, data)
