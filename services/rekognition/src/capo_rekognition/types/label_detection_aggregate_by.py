"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelDetectionAggregateBy``."""

from typing import Literal, TypeAlias, cast

LabelDetectionAggregateBy: TypeAlias = Literal[
    "TIMESTAMPS",
    "SEGMENTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelDetectionAggregateBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LabelDetectionAggregateBy:
    return cast(LabelDetectionAggregateBy, data)
