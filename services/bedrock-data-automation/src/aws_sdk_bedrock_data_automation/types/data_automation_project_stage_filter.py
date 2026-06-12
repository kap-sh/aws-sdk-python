"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectStageFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Project Stage filter"""
DataAutomationProjectStageFilter: TypeAlias = Literal[
    "DEVELOPMENT",
    "LIVE",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEVELOPMENT",
        "LIVE",
        "ALL",
    )
)


def serialize_json(value: DataAutomationProjectStageFilter) -> str:
    return value


def deserialize_json(data: str) -> DataAutomationProjectStageFilter:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataAutomationProjectStageFilter value: {data!r}"
        )
    return cast(DataAutomationProjectStageFilter, data)
