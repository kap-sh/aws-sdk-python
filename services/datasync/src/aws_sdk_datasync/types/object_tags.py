"""Generated from Smithy shape ``com.amazonaws.datasync#ObjectTags``."""

from typing import Literal, TypeAlias, cast

ObjectTags: TypeAlias = Literal[
    "PRESERVE",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectTags) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectTags:
    return cast(ObjectTags, data)
