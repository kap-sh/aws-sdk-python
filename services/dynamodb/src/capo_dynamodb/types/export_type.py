"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportType``."""

from typing import Literal, TypeAlias, cast

ExportType: TypeAlias = Literal[
    "FULL_EXPORT",
    "INCREMENTAL_EXPORT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportType:
    return cast(ExportType, data)
