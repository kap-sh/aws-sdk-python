"""Generated from Smithy shape ``com.amazonaws.rekognition#CelebrityRecognitionSortBy``."""

from typing import Literal, TypeAlias, cast

CelebrityRecognitionSortBy: TypeAlias = Literal[
    "ID",
    "TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CelebrityRecognitionSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CelebrityRecognitionSortBy:
    return cast(CelebrityRecognitionSortBy, data)
