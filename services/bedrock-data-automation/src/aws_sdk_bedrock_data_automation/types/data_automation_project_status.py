"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectStatus``."""

from typing import Literal, TypeAlias, cast

"""Status of Data Automation Project"""
DataAutomationProjectStatus: TypeAlias = Literal[
    "COMPLETED",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationProjectStatus) -> str:
    return value


def deserialize_json(data: str) -> DataAutomationProjectStatus:
    return cast(DataAutomationProjectStatus, data)
