"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#ReportVersioning``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

ReportVersioning: TypeAlias = Literal[
    "CREATE_NEW_REPORT",
    "OVERWRITE_REPORT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_NEW_REPORT",
        "OVERWRITE_REPORT",
    )
)


def serialize_aws_json_1_1(value: ReportVersioning) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportVersioning:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportVersioning value: {data!r}")
    return cast(ReportVersioning, data)
