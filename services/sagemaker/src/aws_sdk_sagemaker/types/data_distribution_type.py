"""Generated from Smithy shape ``com.amazonaws.sagemaker#DataDistributionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

DataDistributionType: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: DataDistributionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataDistributionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataDistributionType value: {data!r}")
    return cast(DataDistributionType, data)
