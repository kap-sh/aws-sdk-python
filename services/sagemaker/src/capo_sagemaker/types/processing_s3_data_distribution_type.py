"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingS3DataDistributionType``."""

from typing import Literal, TypeAlias, cast

ProcessingS3DataDistributionType: TypeAlias = Literal[
    "FullyReplicated",
    "ShardedByS3Key",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingS3DataDistributionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessingS3DataDistributionType:
    return cast(ProcessingS3DataDistributionType, data)
