"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroupSortByType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ReportGroupSortByType: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ReportGroupSortByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportGroupSortByType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportGroupSortByType value: {data!r}")
    return cast(ReportGroupSortByType, data)
