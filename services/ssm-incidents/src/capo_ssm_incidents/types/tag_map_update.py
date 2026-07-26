"""Generated from Smithy shape ``com.amazonaws.ssmincidents#TagMapUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_incidents.types.tag_key
    import capo_ssm_incidents.types.tag_value

TagMapUpdate: TypeAlias = dict[
    "capo_ssm_incidents.types.tag_key.TagKey",
    "capo_ssm_incidents.types.tag_value.TagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TagMapUpdate) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TagMapUpdate:
    out: TagMapUpdate = {}
    for key, value in data.items():
        out[key] = value
    return out
