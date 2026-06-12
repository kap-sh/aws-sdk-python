"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ReportStatusType: TypeAlias = Literal[
    "GENERATING",
    "SUCCEEDED",
    "FAILED",
    "INCOMPLETE",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GENERATING",
        "SUCCEEDED",
        "FAILED",
        "INCOMPLETE",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: ReportStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportStatusType value: {data!r}")
    return cast(ReportStatusType, data)
