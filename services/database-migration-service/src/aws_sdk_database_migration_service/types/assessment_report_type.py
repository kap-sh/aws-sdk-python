"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AssessmentReportType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

AssessmentReportType: TypeAlias = Literal[
    "pdf",
    "csv",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pdf",
        "csv",
    )
)


def serialize_aws_json_1_1(value: AssessmentReportType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssessmentReportType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssessmentReportType value: {data!r}")
    return cast(AssessmentReportType, data)
