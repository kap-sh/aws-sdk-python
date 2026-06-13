"""Generated from Smithy shape ``com.amazonaws.odb#ResponseTagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.tag_key
    import aws_sdk_odb.types.tag_value

ResponseTagMap: TypeAlias = dict[
    "aws_sdk_odb.types.tag_key.TagKey", "aws_sdk_odb.types.tag_value.TagValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ResponseTagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> ResponseTagMap:
    out: ResponseTagMap = {}
    for key, value in data.items():
        out[key] = value
    return out
