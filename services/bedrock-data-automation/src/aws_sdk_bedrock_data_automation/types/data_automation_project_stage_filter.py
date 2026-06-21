"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectStageFilter``."""

from typing import Literal, TypeAlias, cast

"""Project Stage filter"""
DataAutomationProjectStageFilter: TypeAlias = Literal[
    "DEVELOPMENT",
    "LIVE",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationProjectStageFilter) -> str:
    return value


def deserialize_json(data: str) -> DataAutomationProjectStageFilter:
    return cast(DataAutomationProjectStageFilter, data)
