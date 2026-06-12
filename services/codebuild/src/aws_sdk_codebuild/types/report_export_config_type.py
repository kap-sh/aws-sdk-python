"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportExportConfigType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ReportExportConfigType: TypeAlias = Literal[
    "S3",
    "NO_EXPORT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "NO_EXPORT",
    )
)


def serialize_aws_json_1_1(value: ReportExportConfigType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportExportConfigType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportExportConfigType value: {data!r}")
    return cast(ReportExportConfigType, data)
