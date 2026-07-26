"""Generated from Smithy shape ``com.amazonaws.health#tagSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.tag_key
    import capo_health.types.tag_value

tagSet: TypeAlias = dict[
    "capo_health.types.tag_key.tagKey", "capo_health.types.tag_value.tagValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: tagSet) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> tagSet:
    out: tagSet = {}
    for key, value in data.items():
        out[key] = value
    return out
