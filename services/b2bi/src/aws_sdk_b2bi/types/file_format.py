"""Generated from Smithy shape ``com.amazonaws.b2bi#FileFormat``."""

from typing import Literal, TypeAlias, cast

FileFormat: TypeAlias = Literal[
    "XML",
    "JSON",
    "NOT_USED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FileFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FileFormat:
    return cast(FileFormat, data)
