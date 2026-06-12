"""Generated from Smithy shape ``com.amazonaws.codebuild#CacheMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

CacheMode: TypeAlias = Literal[
    "LOCAL_DOCKER_LAYER_CACHE",
    "LOCAL_SOURCE_CACHE",
    "LOCAL_CUSTOM_CACHE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOCAL_DOCKER_LAYER_CACHE",
        "LOCAL_SOURCE_CACHE",
        "LOCAL_CUSTOM_CACHE",
    )
)


def serialize_aws_json_1_1(value: CacheMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CacheMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CacheMode value: {data!r}")
    return cast(CacheMode, data)
