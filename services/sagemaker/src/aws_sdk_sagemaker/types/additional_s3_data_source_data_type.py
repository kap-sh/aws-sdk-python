"""Generated from Smithy shape ``com.amazonaws.sagemaker#AdditionalS3DataSourceDataType``."""

from typing import Literal, TypeAlias, cast

AdditionalS3DataSourceDataType: TypeAlias = Literal[
    "S3Object",
    "S3Prefix",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalS3DataSourceDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdditionalS3DataSourceDataType:
    return cast(AdditionalS3DataSourceDataType, data)
