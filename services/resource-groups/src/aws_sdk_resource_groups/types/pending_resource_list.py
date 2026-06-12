"""Generated from Smithy shape ``com.amazonaws.resourcegroups#PendingResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.pending_resource

PendingResourceList: TypeAlias = list[
    "aws_sdk_resource_groups.types.pending_resource.PendingResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: PendingResourceList) -> list:
    import aws_sdk_resource_groups.types.pending_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_resource_groups.types.pending_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> PendingResourceList:
    import aws_sdk_resource_groups.types.pending_resource

    out: PendingResourceList = []
    for item in data:
        out.append(
            aws_sdk_resource_groups.types.pending_resource.deserialize_json(item)
        )
    return out
