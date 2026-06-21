"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectStage``."""

from typing import Literal, TypeAlias, cast

"""Stage of the Project"""
DataAutomationProjectStage: TypeAlias = Literal[
    "DEVELOPMENT",
    "LIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationProjectStage) -> str:
    return value


def deserialize_json(data: str) -> DataAutomationProjectStage:
    return cast(DataAutomationProjectStage, data)
