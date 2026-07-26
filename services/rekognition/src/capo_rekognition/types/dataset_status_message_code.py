"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetStatusMessageCode``."""

from typing import Literal, TypeAlias, cast

DatasetStatusMessageCode: TypeAlias = Literal[
    "SUCCESS",
    "SERVICE_ERROR",
    "CLIENT_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetStatusMessageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatasetStatusMessageCode:
    return cast(DatasetStatusMessageCode, data)
