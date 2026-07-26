"""Generated from Smithy shape ``com.amazonaws.fsx#ReportFormat``."""

from typing import Literal, TypeAlias, cast

ReportFormat: TypeAlias = Literal["REPORT_CSV_20191124",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportFormat:
    return cast(ReportFormat, data)
