"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.property_definition_response

PropertyDefinitionsResponse: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.property_definition_response.PropertyDefinitionResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PropertyDefinitionsResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.property_definition_response

        out[key] = capo_iottwinmaker.types.property_definition_response.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> PropertyDefinitionsResponse:
    out: PropertyDefinitionsResponse = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.property_definition_response

        out[key] = (
            capo_iottwinmaker.types.property_definition_response.deserialize_json(value)
        )
    return out
