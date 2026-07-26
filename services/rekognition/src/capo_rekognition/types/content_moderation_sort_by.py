"""Generated from Smithy shape ``com.amazonaws.rekognition#ContentModerationSortBy``."""

from typing import Literal, TypeAlias, cast

ContentModerationSortBy: TypeAlias = Literal[
    "NAME",
    "TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentModerationSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContentModerationSortBy:
    return cast(ContentModerationSortBy, data)
