"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DataValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.data_value
    import capo_iottwinmaker.types.string

DataValueMap: TypeAlias = dict[
    "capo_iottwinmaker.types.string.String",
    "capo_iottwinmaker.types.data_value.DataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DataValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.data_value

        out[key] = capo_iottwinmaker.types.data_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> DataValueMap:
    out: DataValueMap = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.data_value

        out[key] = capo_iottwinmaker.types.data_value.deserialize_json(value)
    return out
