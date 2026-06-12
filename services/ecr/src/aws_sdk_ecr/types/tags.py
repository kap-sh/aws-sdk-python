"""Generated from Smithy shape ``com.amazonaws.ecr#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.tag_key
    import aws_sdk_ecr.types.tag_value

Tags: TypeAlias = dict[
    "aws_sdk_ecr.types.tag_key.TagKey", "aws_sdk_ecr.types.tag_value.TagValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        out[key] = value
    return out
