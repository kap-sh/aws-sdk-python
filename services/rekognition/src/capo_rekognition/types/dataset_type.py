"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetType``."""

from typing import Literal, TypeAlias, cast

DatasetType: TypeAlias = Literal[
    "TRAIN",
    "TEST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatasetType:
    return cast(DatasetType, data)
