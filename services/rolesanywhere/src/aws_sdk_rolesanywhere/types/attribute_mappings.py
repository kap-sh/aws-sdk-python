"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#AttributeMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.attribute_mapping

AttributeMappings: TypeAlias = list[
    "aws_sdk_rolesanywhere.types.attribute_mapping.AttributeMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeMappings) -> list:
    import aws_sdk_rolesanywhere.types.attribute_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_rolesanywhere.types.attribute_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributeMappings:
    import aws_sdk_rolesanywhere.types.attribute_mapping

    out: AttributeMappings = []
    for item in data:
        out.append(aws_sdk_rolesanywhere.types.attribute_mapping.deserialize_json(item))
    return out
