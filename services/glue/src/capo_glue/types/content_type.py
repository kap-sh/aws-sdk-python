"""Generated from Smithy shape ``com.amazonaws.glue#ContentType``."""

from typing import Literal, TypeAlias, cast

ContentType: TypeAlias = Literal[
    "APPLICATION_JSON",
    "URL_ENCODED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContentType:
    return cast(ContentType, data)
