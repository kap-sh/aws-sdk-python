"""Generated from Smithy shape ``com.amazonaws.evs#RequestTagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_evs.types.tag_key
    import aws_sdk_evs.types.tag_value

RequestTagMap: TypeAlias = dict[
    "aws_sdk_evs.types.tag_key.TagKey", "aws_sdk_evs.types.tag_value.TagValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RequestTagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestTagMap:
    out: RequestTagMap = {}
    for key, value in data.items():
        out[key] = value
    return out
