"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyDefinitionsRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.property_definition_request

PropertyDefinitionsRequest: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.property_definition_request.PropertyDefinitionRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PropertyDefinitionsRequest) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.property_definition_request

        out[key] = capo_iottwinmaker.types.property_definition_request.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> PropertyDefinitionsRequest:
    out: PropertyDefinitionsRequest = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.property_definition_request

        out[key] = capo_iottwinmaker.types.property_definition_request.deserialize_json(
            value
        )
    return out
