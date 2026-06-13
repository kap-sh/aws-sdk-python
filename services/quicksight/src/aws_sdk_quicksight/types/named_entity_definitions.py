"""Generated from Smithy shape ``com.amazonaws.quicksight#NamedEntityDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.named_entity_definition

NamedEntityDefinitions: TypeAlias = list[
    "aws_sdk_quicksight.types.named_entity_definition.NamedEntityDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: NamedEntityDefinitions) -> list:
    import aws_sdk_quicksight.types.named_entity_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.named_entity_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NamedEntityDefinitions:
    import aws_sdk_quicksight.types.named_entity_definition

    out: NamedEntityDefinitions = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.named_entity_definition.deserialize_json(item)
        )
    return out
