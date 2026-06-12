"""Generated from Smithy shape ``com.amazonaws.sagemaker#S3DataDistribution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

S3DataDistribution: TypeAlias = Literal[
    "FullyReplicated",
    "ShardedByS3Key",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FullyReplicated",
        "ShardedByS3Key",
    )
)


def serialize_aws_json_1_1(value: S3DataDistribution) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3DataDistribution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3DataDistribution value: {data!r}")
    return cast(S3DataDistribution, data)
