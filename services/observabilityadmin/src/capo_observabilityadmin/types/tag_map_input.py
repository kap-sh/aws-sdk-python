"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TagMapInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.tag_key
    import capo_observabilityadmin.types.tag_value

TagMapInput: TypeAlias = dict[
    "capo_observabilityadmin.types.tag_key.TagKey",
    "capo_observabilityadmin.types.tag_value.TagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TagMapInput) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TagMapInput:
    out: TagMapInput = {}
    for key, value in data.items():
        out[key] = value
    return out
