"""Generated from Smithy shape ``com.amazonaws.transfer#CompressionEnum``."""

from typing import Literal, TypeAlias, cast

CompressionEnum: TypeAlias = Literal[
    "ZLIB",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompressionEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompressionEnum:
    return cast(CompressionEnum, data)
