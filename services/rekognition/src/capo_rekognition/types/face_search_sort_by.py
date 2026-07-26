"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceSearchSortBy``."""

from typing import Literal, TypeAlias, cast

FaceSearchSortBy: TypeAlias = Literal[
    "INDEX",
    "TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceSearchSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FaceSearchSortBy:
    return cast(FaceSearchSortBy, data)
