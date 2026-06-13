"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#InstanceProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.instance_property

InstanceProperties: TypeAlias = list[
    "aws_sdk_rolesanywhere.types.instance_property.InstanceProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceProperties) -> list:
    import aws_sdk_rolesanywhere.types.instance_property

    out: list = []
    for item in value:
        out.append(aws_sdk_rolesanywhere.types.instance_property.serialize_json(item))
    return out


def deserialize_json(data: list) -> InstanceProperties:
    import aws_sdk_rolesanywhere.types.instance_property

    out: InstanceProperties = []
    for item in data:
        out.append(aws_sdk_rolesanywhere.types.instance_property.deserialize_json(item))
    return out
