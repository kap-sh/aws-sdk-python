"""Generated from Smithy shape ``com.amazonaws.ram#ResourceSharePermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ram.types.resource_share_permission_summary

ResourceSharePermissionList: TypeAlias = list[
    "aws_sdk_ram.types.resource_share_permission_summary.ResourceSharePermissionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSharePermissionList) -> list:
    import aws_sdk_ram.types.resource_share_permission_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ram.types.resource_share_permission_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourceSharePermissionList:
    import aws_sdk_ram.types.resource_share_permission_summary

    out: ResourceSharePermissionList = []
    for item in data:
        out.append(
            aws_sdk_ram.types.resource_share_permission_summary.deserialize_json(item)
        )
    return out
