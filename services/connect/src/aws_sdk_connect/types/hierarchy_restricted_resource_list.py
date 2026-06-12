"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyRestrictedResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_restricted_resource_name

HierarchyRestrictedResourceList: TypeAlias = list[
    "aws_sdk_connect.types.hierarchy_restricted_resource_name.HierarchyRestrictedResourceName"
]


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyRestrictedResourceList) -> list:
    return list(value)


def deserialize_json(data: list) -> HierarchyRestrictedResourceList:
    return list(data)
