"""Generated from Smithy shape ``com.amazonaws.textract#TagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.tag_key
    import aws_sdk_textract.types.tag_value

TagMap: TypeAlias = dict[
    "aws_sdk_textract.types.tag_key.TagKey", "aws_sdk_textract.types.tag_value.TagValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> TagMap:
    out: TagMap = {}
    for key, value in data.items():
        out[key] = value
    return out
