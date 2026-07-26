"""Generated from Smithy shape ``com.amazonaws.firehose#ContentEncoding``."""

from typing import Literal, TypeAlias, cast

ContentEncoding: TypeAlias = Literal[
    "NONE",
    "GZIP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentEncoding) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContentEncoding:
    return cast(ContentEncoding, data)
