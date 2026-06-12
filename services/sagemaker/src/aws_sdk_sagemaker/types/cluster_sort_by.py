"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterSortBy: TypeAlias = Literal[
    "CREATION_TIME",
    "NAME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATION_TIME",
        "NAME",
    )
)


def serialize_aws_json_1_1(value: ClusterSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterSortBy value: {data!r}")
    return cast(ClusterSortBy, data)
