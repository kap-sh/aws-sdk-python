"""Generated from Smithy shape ``com.amazonaws.pcs#RequestTagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pcs.types.tag_key
    import capo_pcs.types.tag_value

RequestTagMap: TypeAlias = dict[
    "capo_pcs.types.tag_key.TagKey", "capo_pcs.types.tag_value.TagValue"
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
