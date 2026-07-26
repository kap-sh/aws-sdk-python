"""Generated from Smithy shape ``com.amazonaws.firehose#OrcCompression``."""

from typing import Literal, TypeAlias, cast

OrcCompression: TypeAlias = Literal[
    "NONE",
    "ZLIB",
    "SNAPPY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrcCompression) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrcCompression:
    return cast(OrcCompression, data)
