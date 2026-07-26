"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#ReportVersioning``."""

from typing import Literal, TypeAlias, cast

ReportVersioning: TypeAlias = Literal[
    "CREATE_NEW_REPORT",
    "OVERWRITE_REPORT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportVersioning) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportVersioning:
    return cast(ReportVersioning, data)
