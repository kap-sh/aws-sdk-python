"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortPipelinesBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortPipelinesBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
    )
)


def serialize_aws_json_1_1(value: SortPipelinesBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortPipelinesBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortPipelinesBy value: {data!r}")
    return cast(SortPipelinesBy, data)
