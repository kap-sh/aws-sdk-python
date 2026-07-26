"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectType``."""

from typing import Literal, TypeAlias, cast

"""Type of the DataAutomationProject"""
DataAutomationProjectType: TypeAlias = Literal[
    "ASYNC",
    "SYNC",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationProjectType) -> str:
    return value


def deserialize_json(data: str) -> DataAutomationProjectType:
    return cast(DataAutomationProjectType, data)
