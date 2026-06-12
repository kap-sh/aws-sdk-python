"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.name
    import aws_sdk_iottwinmaker.types.property_definition_response

PropertyDefinitionsResponse: TypeAlias = dict[
    "aws_sdk_iottwinmaker.types.name.Name",
    "aws_sdk_iottwinmaker.types.property_definition_response.PropertyDefinitionResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PropertyDefinitionsResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iottwinmaker.types.property_definition_response

        out[key] = (
            aws_sdk_iottwinmaker.types.property_definition_response.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> PropertyDefinitionsResponse:
    out: PropertyDefinitionsResponse = {}
    for key, value in data.items():
        import aws_sdk_iottwinmaker.types.property_definition_response

        out[key] = (
            aws_sdk_iottwinmaker.types.property_definition_response.deserialize_json(
                value
            )
        )
    return out
