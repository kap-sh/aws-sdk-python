"""Generated from Smithy shape ``com.amazonaws.odb#OpenMode``."""

from typing import Literal, TypeAlias, cast

OpenMode: TypeAlias = Literal[
    "READ_ONLY",
    "READ_WRITE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpenMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OpenMode:
    return cast(OpenMode, data)
