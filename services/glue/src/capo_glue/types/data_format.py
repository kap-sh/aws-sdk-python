"""Generated from Smithy shape ``com.amazonaws.glue#DataFormat``."""

from typing import Literal, TypeAlias, cast

DataFormat: TypeAlias = Literal[
    "AVRO",
    "JSON",
    "PROTOBUF",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataFormat:
    return cast(DataFormat, data)
