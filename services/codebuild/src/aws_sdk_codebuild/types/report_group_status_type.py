"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroupStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ReportGroupStatusType: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: ReportGroupStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportGroupStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportGroupStatusType value: {data!r}")
    return cast(ReportGroupStatusType, data)
