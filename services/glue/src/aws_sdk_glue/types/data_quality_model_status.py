"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityModelStatus``."""

from typing import Literal, TypeAlias, cast

DataQualityModelStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityModelStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataQualityModelStatus:
    return cast(DataQualityModelStatus, data)
