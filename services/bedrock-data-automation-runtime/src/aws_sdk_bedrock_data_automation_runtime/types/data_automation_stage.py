"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#DataAutomationStage``."""

from typing import Literal, TypeAlias, cast

"""Data automation stage."""
DataAutomationStage: TypeAlias = Literal[
    "LIVE",
    "DEVELOPMENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataAutomationStage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataAutomationStage:
    return cast(DataAutomationStage, data)
