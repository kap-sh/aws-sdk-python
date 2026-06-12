"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Status of Data Automation Project"""
DataAutomationProjectStatus: TypeAlias = Literal[
    "COMPLETED",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "IN_PROGRESS",
        "FAILED",
    )
)


def serialize_json(value: DataAutomationProjectStatus) -> str:
    return value


def deserialize_json(data: str) -> DataAutomationProjectStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataAutomationProjectStatus value: {data!r}"
        )
    return cast(DataAutomationProjectStatus, data)
