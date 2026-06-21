"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#S3OutputType``."""

from typing import Literal, TypeAlias, cast

S3OutputType: TypeAlias = Literal[
    "CUSTOM",
    "ATHENA",
    "REDSHIFT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3OutputType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3OutputType:
    return cast(S3OutputType, data)
