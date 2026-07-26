"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.property_request

PropertyRequests: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.property_request.PropertyRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PropertyRequests) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.property_request

        out[key] = capo_iottwinmaker.types.property_request.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PropertyRequests:
    out: PropertyRequests = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.property_request

        out[key] = capo_iottwinmaker.types.property_request.deserialize_json(value)
    return out
