"""Generated from Smithy shape ``com.amazonaws.applicationsignals#GroupingAttributeDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.grouping_attribute_definition

GroupingAttributeDefinitions: TypeAlias = list[
    "capo_application_signals.types.grouping_attribute_definition.GroupingAttributeDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingAttributeDefinitions) -> list:
    import capo_application_signals.types.grouping_attribute_definition

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.grouping_attribute_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GroupingAttributeDefinitions:
    import capo_application_signals.types.grouping_attribute_definition

    out: GroupingAttributeDefinitions = []
    for item in data:
        out.append(
            capo_application_signals.types.grouping_attribute_definition.deserialize_json(
                item
            )
        )
    return out
