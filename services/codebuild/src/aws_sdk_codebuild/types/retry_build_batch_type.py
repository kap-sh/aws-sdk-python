"""Generated from Smithy shape ``com.amazonaws.codebuild#RetryBuildBatchType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

RetryBuildBatchType: TypeAlias = Literal[
    "RETRY_ALL_BUILDS",
    "RETRY_FAILED_BUILDS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RETRY_ALL_BUILDS",
        "RETRY_FAILED_BUILDS",
    )
)


def serialize_aws_json_1_1(value: RetryBuildBatchType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RetryBuildBatchType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetryBuildBatchType value: {data!r}")
    return cast(RetryBuildBatchType, data)
