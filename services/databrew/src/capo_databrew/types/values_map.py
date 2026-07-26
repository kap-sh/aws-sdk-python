"""Generated from Smithy shape ``com.amazonaws.databrew#ValuesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.condition_value
    import capo_databrew.types.value_reference

ValuesMap: TypeAlias = dict[
    "capo_databrew.types.value_reference.ValueReference",
    "capo_databrew.types.condition_value.ConditionValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ValuesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ValuesMap:
    out: ValuesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
