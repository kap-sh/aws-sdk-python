"""Generated from Smithy shape ``com.amazonaws.rekognition#VideoColorRange``."""

from typing import Literal, TypeAlias, cast

VideoColorRange: TypeAlias = Literal[
    "FULL",
    "LIMITED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VideoColorRange) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VideoColorRange:
    return cast(VideoColorRange, data)
