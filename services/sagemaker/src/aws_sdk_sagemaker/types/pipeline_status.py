"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

PipelineStatus: TypeAlias = Literal[
    "Active",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Deleting",
    )
)


def serialize_aws_json_1_1(value: PipelineStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PipelineStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PipelineStatus value: {data!r}")
    return cast(PipelineStatus, data)
