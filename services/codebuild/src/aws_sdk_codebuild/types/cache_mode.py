"""Generated from Smithy shape ``com.amazonaws.codebuild#CacheMode``."""

from typing import Literal, TypeAlias, cast

CacheMode: TypeAlias = Literal[
    "LOCAL_DOCKER_LAYER_CACHE",
    "LOCAL_SOURCE_CACHE",
    "LOCAL_CUSTOM_CACHE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CacheMode:
    return cast(CacheMode, data)
