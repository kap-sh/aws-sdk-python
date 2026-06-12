"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Type of the DataAutomationProject"""
DataAutomationProjectType: TypeAlias = Literal[
    "ASYNC",
    "SYNC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASYNC",
        "SYNC",
    )
)


def serialize_json(value: DataAutomationProjectType) -> str:
    return value


def deserialize_json(data: str) -> DataAutomationProjectType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataAutomationProjectType value: {data!r}")
    return cast(DataAutomationProjectType, data)
