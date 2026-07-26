"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups.types.group_identifier

GroupIdentifierList: TypeAlias = list[
    "capo_resource_groups.types.group_identifier.GroupIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupIdentifierList) -> list:
    import capo_resource_groups.types.group_identifier

    out: list = []
    for item in value:
        out.append(capo_resource_groups.types.group_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupIdentifierList:
    import capo_resource_groups.types.group_identifier

    out: GroupIdentifierList = []
    for item in data:
        out.append(capo_resource_groups.types.group_identifier.deserialize_json(item))
    return out
