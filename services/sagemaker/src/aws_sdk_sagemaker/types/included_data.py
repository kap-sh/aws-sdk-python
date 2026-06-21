"""Generated from Smithy shape ``com.amazonaws.sagemaker#IncludedData``."""

from typing import Literal, TypeAlias, cast

IncludedData: TypeAlias = Literal[
    "AllData",
    "MetadataOnly",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncludedData) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IncludedData:
    return cast(IncludedData, data)
