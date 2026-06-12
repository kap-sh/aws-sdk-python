"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortPipelineExecutionsBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortPipelineExecutionsBy: TypeAlias = Literal[
    "CreationTime",
    "PipelineExecutionArn",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreationTime",
        "PipelineExecutionArn",
    )
)


def serialize_aws_json_1_1(value: SortPipelineExecutionsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortPipelineExecutionsBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortPipelineExecutionsBy value: {data!r}")
    return cast(SortPipelineExecutionsBy, data)
