"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectStage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Stage of the Project"""
DataAutomationProjectStage: TypeAlias = Literal[
    "DEVELOPMENT",
    "LIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEVELOPMENT",
        "LIVE",
    )
)


def serialize_json(value: DataAutomationProjectStage) -> str:
    return value


def deserialize_json(data: str) -> DataAutomationProjectStage:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataAutomationProjectStage value: {data!r}"
        )
    return cast(DataAutomationProjectStage, data)
