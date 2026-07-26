"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelDetectionSortBy``."""

from typing import Literal, TypeAlias, cast

LabelDetectionSortBy: TypeAlias = Literal[
    "NAME",
    "TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelDetectionSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LabelDetectionSortBy:
    return cast(LabelDetectionSortBy, data)
