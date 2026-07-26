"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyTableValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.data_value
    import capo_iottwinmaker.types.name

PropertyTableValue: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name", "capo_iottwinmaker.types.data_value.DataValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PropertyTableValue) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.data_value

        out[key] = capo_iottwinmaker.types.data_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PropertyTableValue:
    out: PropertyTableValue = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.data_value

        out[key] = capo_iottwinmaker.types.data_value.deserialize_json(value)
    return out
