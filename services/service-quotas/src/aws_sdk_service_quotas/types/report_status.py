"""Generated from Smithy shape ``com.amazonaws.servicequotas#ReportStatus``."""

from typing import Literal, TypeAlias, cast

ReportStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportStatus:
    return cast(ReportStatus, data)
