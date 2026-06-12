"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProjectSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ProjectSortBy: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ProjectSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProjectSortBy value: {data!r}")
    return cast(ProjectSortBy, data)
