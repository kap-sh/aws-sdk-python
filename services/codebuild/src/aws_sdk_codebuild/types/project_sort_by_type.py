"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectSortByType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ProjectSortByType: TypeAlias = Literal[
    "NAME",
    "CREATED_TIME",
    "LAST_MODIFIED_TIME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "CREATED_TIME",
        "LAST_MODIFIED_TIME",
    )
)


def serialize_aws_json_1_1(value: ProjectSortByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectSortByType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProjectSortByType value: {data!r}")
    return cast(ProjectSortByType, data)
