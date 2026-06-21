"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#ReportFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The format that Amazon Web Services saves the report in.</p>"""
ReportFormat: TypeAlias = Literal[
    "textORcsv",
    "Parquet",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportFormat:
    return cast(ReportFormat, data)
