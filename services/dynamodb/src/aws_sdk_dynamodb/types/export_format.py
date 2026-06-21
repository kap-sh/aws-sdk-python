"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportFormat``."""

from typing import Literal, TypeAlias, cast

ExportFormat: TypeAlias = Literal[
    "DYNAMODB_JSON",
    "ION",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportFormat:
    return cast(ExportFormat, data)
