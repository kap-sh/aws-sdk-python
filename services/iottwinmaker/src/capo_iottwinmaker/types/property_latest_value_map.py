"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyLatestValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.property_latest_value

PropertyLatestValueMap: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.property_latest_value.PropertyLatestValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PropertyLatestValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.property_latest_value

        out[key] = capo_iottwinmaker.types.property_latest_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PropertyLatestValueMap:
    out: PropertyLatestValueMap = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.property_latest_value

        out[key] = capo_iottwinmaker.types.property_latest_value.deserialize_json(value)
    return out
