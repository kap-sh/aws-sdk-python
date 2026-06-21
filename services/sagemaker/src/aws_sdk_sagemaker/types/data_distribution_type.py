"""Generated from Smithy shape ``com.amazonaws.sagemaker#DataDistributionType``."""

from typing import Literal, TypeAlias, cast

DataDistributionType: TypeAlias = Literal[
    "FullyReplicated",
    "ShardedByS3Key",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataDistributionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataDistributionType:
    return cast(DataDistributionType, data)
