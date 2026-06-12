"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#ReportFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

"""<p>The format that Amazon Web Services saves the report in.</p>"""
ReportFormat: TypeAlias = Literal[
    "textORcsv",
    "Parquet",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "textORcsv",
        "Parquet",
    )
)


def serialize_aws_json_1_1(value: ReportFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportFormat value: {data!r}")
    return cast(ReportFormat, data)
