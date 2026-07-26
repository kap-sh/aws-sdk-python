"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AssessmentReportType``."""

from typing import Literal, TypeAlias, cast

AssessmentReportType: TypeAlias = Literal[
    "pdf",
    "csv",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentReportType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssessmentReportType:
    return cast(AssessmentReportType, data)
