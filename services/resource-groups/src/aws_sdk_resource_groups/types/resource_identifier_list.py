"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ResourceIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.resource_identifier

ResourceIdentifierList: TypeAlias = list[
    "aws_sdk_resource_groups.types.resource_identifier.ResourceIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceIdentifierList) -> list:
    import aws_sdk_resource_groups.types.resource_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resource_groups.types.resource_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourceIdentifierList:
    import aws_sdk_resource_groups.types.resource_identifier

    out: ResourceIdentifierList = []
    for item in data:
        out.append(
            aws_sdk_resource_groups.types.resource_identifier.deserialize_json(item)
        )
    return out
