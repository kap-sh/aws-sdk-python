"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

JobType: TypeAlias = Literal[
    "TRAINING",
    "INFERENCE",
    "NOTEBOOK_KERNEL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRAINING",
        "INFERENCE",
        "NOTEBOOK_KERNEL",
    )
)


def serialize_aws_json_1_1(value: JobType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobType value: {data!r}")
    return cast(JobType, data)
