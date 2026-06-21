"""Generated from Smithy shape ``com.amazonaws.inspector#ReportFileFormat``."""

from typing import Literal, TypeAlias, cast

ReportFileFormat: TypeAlias = Literal[
    "HTML",
    "PDF",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportFileFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportFileFormat:
    return cast(ReportFileFormat, data)
