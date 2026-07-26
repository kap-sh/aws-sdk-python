"""Generated from Smithy shape ``com.amazonaws.inspector#ReportType``."""

from typing import Literal, TypeAlias, cast

ReportType: TypeAlias = Literal[
    "FINDING",
    "FULL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportType:
    return cast(ReportType, data)
