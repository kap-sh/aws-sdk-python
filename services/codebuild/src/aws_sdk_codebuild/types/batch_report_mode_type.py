"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchReportModeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

BatchReportModeType: TypeAlias = Literal[
    "REPORT_INDIVIDUAL_BUILDS",
    "REPORT_AGGREGATED_BATCH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REPORT_INDIVIDUAL_BUILDS",
        "REPORT_AGGREGATED_BATCH",
    )
)


def serialize_aws_json_1_1(value: BatchReportModeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchReportModeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchReportModeType value: {data!r}")
    return cast(BatchReportModeType, data)
