"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortClusterSchedulerConfigBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortClusterSchedulerConfigBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
        "Status",
    )
)


def serialize_aws_json_1_1(value: SortClusterSchedulerConfigBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortClusterSchedulerConfigBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SortClusterSchedulerConfigBy value: {data!r}"
        )
    return cast(SortClusterSchedulerConfigBy, data)
