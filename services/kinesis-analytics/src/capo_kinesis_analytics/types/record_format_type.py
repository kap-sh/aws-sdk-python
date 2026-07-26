"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#RecordFormatType``."""

from typing import Literal, TypeAlias, cast

RecordFormatType: TypeAlias = Literal[
    "JSON",
    "CSV",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordFormatType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordFormatType:
    return cast(RecordFormatType, data)
