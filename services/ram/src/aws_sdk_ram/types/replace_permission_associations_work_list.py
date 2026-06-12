"""Generated from Smithy shape ``com.amazonaws.ram#ReplacePermissionAssociationsWorkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ram.types.replace_permission_associations_work

ReplacePermissionAssociationsWorkList: TypeAlias = list[
    "aws_sdk_ram.types.replace_permission_associations_work.ReplacePermissionAssociationsWork"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplacePermissionAssociationsWorkList) -> list:
    import aws_sdk_ram.types.replace_permission_associations_work

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ram.types.replace_permission_associations_work.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReplacePermissionAssociationsWorkList:
    import aws_sdk_ram.types.replace_permission_associations_work

    out: ReplacePermissionAssociationsWorkList = []
    for item in data:
        out.append(
            aws_sdk_ram.types.replace_permission_associations_work.deserialize_json(
                item
            )
        )
    return out
