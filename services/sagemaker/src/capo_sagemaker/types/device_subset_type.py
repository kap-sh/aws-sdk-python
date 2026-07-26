"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceSubsetType``."""

from typing import Literal, TypeAlias, cast

DeviceSubsetType: TypeAlias = Literal[
    "PERCENTAGE",
    "SELECTION",
    "NAMECONTAINS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceSubsetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceSubsetType:
    return cast(DeviceSubsetType, data)
