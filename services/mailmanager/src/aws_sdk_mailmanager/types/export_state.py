"""Generated from Smithy shape ``com.amazonaws.mailmanager#ExportState``."""

from typing import Literal, TypeAlias, cast

ExportState: TypeAlias = Literal[
    "QUEUED",
    "PREPROCESSING",
    "PROCESSING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportState:
    return cast(ExportState, data)
