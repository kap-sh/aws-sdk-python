"""Generated from Smithy shape ``com.amazonaws.resourcegroups#FailedResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups.types.failed_resource

FailedResourceList: TypeAlias = list[
    "capo_resource_groups.types.failed_resource.FailedResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedResourceList) -> list:
    import capo_resource_groups.types.failed_resource

    out: list = []
    for item in value:
        out.append(capo_resource_groups.types.failed_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> FailedResourceList:
    import capo_resource_groups.types.failed_resource

    out: FailedResourceList = []
    for item in data:
        out.append(capo_resource_groups.types.failed_resource.deserialize_json(item))
    return out
