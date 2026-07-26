"""Generated from Smithy shape ``com.amazonaws.sfn#InspectionLevel``."""

from typing import Literal, TypeAlias, cast

InspectionLevel: TypeAlias = Literal[
    "INFO",
    "DEBUG",
    "TRACE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InspectionLevel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InspectionLevel:
    return cast(InspectionLevel, data)
