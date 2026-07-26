"""Generated from Smithy shape ``com.amazonaws.kms#DataKeySpec``."""

from typing import Literal, TypeAlias, cast

DataKeySpec: TypeAlias = Literal[
    "AES_256",
    "AES_128",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataKeySpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataKeySpec:
    return cast(DataKeySpec, data)
