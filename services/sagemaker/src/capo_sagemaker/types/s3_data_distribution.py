"""Generated from Smithy shape ``com.amazonaws.sagemaker#S3DataDistribution``."""

from typing import Literal, TypeAlias, cast

S3DataDistribution: TypeAlias = Literal[
    "FullyReplicated",
    "ShardedByS3Key",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DataDistribution) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3DataDistribution:
    return cast(S3DataDistribution, data)
