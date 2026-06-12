"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_identifier

GroupIdentifierList: TypeAlias = list[
    "aws_sdk_resource_groups.types.group_identifier.GroupIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupIdentifierList) -> list:
    import aws_sdk_resource_groups.types.group_identifier

    out: list = []
    for item in value:
        out.append(aws_sdk_resource_groups.types.group_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupIdentifierList:
    import aws_sdk_resource_groups.types.group_identifier

    out: GroupIdentifierList = []
    for item in data:
        out.append(
            aws_sdk_resource_groups.types.group_identifier.deserialize_json(item)
        )
    return out
