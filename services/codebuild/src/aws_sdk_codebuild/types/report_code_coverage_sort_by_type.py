"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportCodeCoverageSortByType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ReportCodeCoverageSortByType: TypeAlias = Literal[
    "LINE_COVERAGE_PERCENTAGE",
    "FILE_PATH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINE_COVERAGE_PERCENTAGE",
        "FILE_PATH",
    )
)


def serialize_aws_json_1_1(value: ReportCodeCoverageSortByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportCodeCoverageSortByType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReportCodeCoverageSortByType value: {data!r}"
        )
    return cast(ReportCodeCoverageSortByType, data)
