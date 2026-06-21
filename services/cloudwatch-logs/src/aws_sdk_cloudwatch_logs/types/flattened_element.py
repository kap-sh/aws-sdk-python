"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#FlattenedElement``."""

from typing import Literal, TypeAlias, cast

FlattenedElement: TypeAlias = Literal[
    "first",
    "last",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlattenedElement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlattenedElement:
    return cast(FlattenedElement, data)
