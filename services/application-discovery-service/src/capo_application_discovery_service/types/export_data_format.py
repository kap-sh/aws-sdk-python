"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportDataFormat``."""

from typing import Literal, TypeAlias, cast

ExportDataFormat: TypeAlias = Literal["CSV",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportDataFormat:
    return cast(ExportDataFormat, data)
