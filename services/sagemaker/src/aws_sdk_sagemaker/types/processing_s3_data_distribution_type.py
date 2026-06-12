"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingS3DataDistributionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ProcessingS3DataDistributionType: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ProcessingS3DataDistributionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessingS3DataDistributionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProcessingS3DataDistributionType value: {data!r}"
        )
    return cast(ProcessingS3DataDistributionType, data)
