"""Generated from Smithy shape ``com.amazonaws.amp#LabelSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amp.types.label_name
    import capo_amp.types.label_value

LabelSet: TypeAlias = dict[
    "capo_amp.types.label_name.LabelName", "capo_amp.types.label_value.LabelValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LabelSet) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> LabelSet:
    out: LabelSet = {}
    for key, value in data.items():
        out[key] = value
    return out
