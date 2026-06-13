"""Generated from Smithy shape ``com.amazonaws.applicationsignals#GroupingAttributeDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.grouping_attribute_definition

GroupingAttributeDefinitions: TypeAlias = list[
    "aws_sdk_application_signals.types.grouping_attribute_definition.GroupingAttributeDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingAttributeDefinitions) -> list:
    import aws_sdk_application_signals.types.grouping_attribute_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_signals.types.grouping_attribute_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GroupingAttributeDefinitions:
    import aws_sdk_application_signals.types.grouping_attribute_definition

    out: GroupingAttributeDefinitions = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.grouping_attribute_definition.deserialize_json(
                item
            )
        )
    return out
