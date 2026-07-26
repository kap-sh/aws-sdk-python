"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExportStatusCode``."""

from typing import Literal, TypeAlias, cast

ExportStatusCode: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportStatusCode:
    return cast(ExportStatusCode, data)
