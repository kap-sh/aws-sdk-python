"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ContinuousExportStatus``."""

from typing import Literal, TypeAlias, cast

ContinuousExportStatus: TypeAlias = Literal[
    "START_IN_PROGRESS",
    "START_FAILED",
    "ACTIVE",
    "ERROR",
    "STOP_IN_PROGRESS",
    "STOP_FAILED",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinuousExportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContinuousExportStatus:
    return cast(ContinuousExportStatus, data)
