"""Generated from Smithy shape ``com.amazonaws.ecs#PropagateMITags``."""

from typing import Literal, TypeAlias, cast

PropagateMITags: TypeAlias = Literal[
    "CAPACITY_PROVIDER",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropagateMITags) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PropagateMITags:
    return cast(PropagateMITags, data)
