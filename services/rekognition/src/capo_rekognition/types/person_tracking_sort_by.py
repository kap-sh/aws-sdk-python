"""Generated from Smithy shape ``com.amazonaws.rekognition#PersonTrackingSortBy``."""

from typing import Literal, TypeAlias, cast

PersonTrackingSortBy: TypeAlias = Literal[
    "INDEX",
    "TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonTrackingSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PersonTrackingSortBy:
    return cast(PersonTrackingSortBy, data)
