"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkAttributeDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.typed_link_attribute_definition

TypedLinkAttributeDefinitionList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.typed_link_attribute_definition.TypedLinkAttributeDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkAttributeDefinitionList) -> list:
    import aws_sdk_clouddirectory.types.typed_link_attribute_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_clouddirectory.types.typed_link_attribute_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TypedLinkAttributeDefinitionList:
    import aws_sdk_clouddirectory.types.typed_link_attribute_definition

    out: TypedLinkAttributeDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_clouddirectory.types.typed_link_attribute_definition.deserialize_json(
                item
            )
        )
    return out
