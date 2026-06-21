"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CodeContentType``."""

from typing import Literal, TypeAlias, cast

CodeContentType: TypeAlias = Literal[
    "PLAINTEXT",
    "ZIPFILE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CodeContentType:
    return cast(CodeContentType, data)
