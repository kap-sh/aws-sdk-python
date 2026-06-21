"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#CustomOutputStatus``."""

from typing import Literal, TypeAlias, cast

"""Custom output status enum"""
CustomOutputStatus: TypeAlias = Literal[
    "MATCH",
    "NO_MATCH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomOutputStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomOutputStatus:
    return cast(CustomOutputStatus, data)
