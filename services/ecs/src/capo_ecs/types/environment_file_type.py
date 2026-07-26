"""Generated from Smithy shape ``com.amazonaws.ecs#EnvironmentFileType``."""

from typing import Literal, TypeAlias, cast

EnvironmentFileType: TypeAlias = Literal["s3",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentFileType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnvironmentFileType:
    return cast(EnvironmentFileType, data)
