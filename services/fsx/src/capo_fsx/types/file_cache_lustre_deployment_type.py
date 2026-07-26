"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheLustreDeploymentType``."""

from typing import Literal, TypeAlias, cast

FileCacheLustreDeploymentType: TypeAlias = Literal["CACHE_1",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCacheLustreDeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileCacheLustreDeploymentType:
    return cast(FileCacheLustreDeploymentType, data)
