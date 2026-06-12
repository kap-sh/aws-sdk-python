"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroupTrendFieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ReportGroupTrendFieldType: TypeAlias = Literal[
    "PASS_RATE",
    "DURATION",
    "TOTAL",
    "LINE_COVERAGE",
    "LINES_COVERED",
    "LINES_MISSED",
    "BRANCH_COVERAGE",
    "BRANCHES_COVERED",
    "BRANCHES_MISSED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASS_RATE",
        "DURATION",
        "TOTAL",
        "LINE_COVERAGE",
        "LINES_COVERED",
        "LINES_MISSED",
        "BRANCH_COVERAGE",
        "BRANCHES_COVERED",
        "BRANCHES_MISSED",
    )
)


def serialize_aws_json_1_1(value: ReportGroupTrendFieldType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportGroupTrendFieldType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportGroupTrendFieldType value: {data!r}")
    return cast(ReportGroupTrendFieldType, data)
