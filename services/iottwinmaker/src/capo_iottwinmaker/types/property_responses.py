"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyResponses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.property_response

PropertyResponses: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.property_response.PropertyResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PropertyResponses) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.property_response

        out[key] = capo_iottwinmaker.types.property_response.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PropertyResponses:
    out: PropertyResponses = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.property_response

        out[key] = capo_iottwinmaker.types.property_response.deserialize_json(value)
    return out
