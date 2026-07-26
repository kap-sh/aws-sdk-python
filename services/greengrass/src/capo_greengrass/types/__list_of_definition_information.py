"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfDefinitionInformation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.definition_information

__listOfDefinitionInformation: TypeAlias = list[
    "capo_greengrass.types.definition_information.DefinitionInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDefinitionInformation) -> list:
    import capo_greengrass.types.definition_information

    out: list = []
    for item in value:
        out.append(capo_greengrass.types.definition_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDefinitionInformation:
    import capo_greengrass.types.definition_information

    out: __listOfDefinitionInformation = []
    for item in data:
        out.append(capo_greengrass.types.definition_information.deserialize_json(item))
    return out
