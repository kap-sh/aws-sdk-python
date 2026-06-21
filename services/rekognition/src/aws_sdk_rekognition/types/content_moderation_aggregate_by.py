"""Generated from Smithy shape ``com.amazonaws.rekognition#ContentModerationAggregateBy``."""

from typing import Literal, TypeAlias, cast

ContentModerationAggregateBy: TypeAlias = Literal[
    "TIMESTAMPS",
    "SEGMENTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentModerationAggregateBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContentModerationAggregateBy:
    return cast(ContentModerationAggregateBy, data)
