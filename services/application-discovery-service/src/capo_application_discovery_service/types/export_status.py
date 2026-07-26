"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportStatus``."""

from typing import Literal, TypeAlias, cast

ExportStatus: TypeAlias = Literal[
    "FAILED",
    "SUCCEEDED",
    "IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportStatus:
    return cast(ExportStatus, data)
