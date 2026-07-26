"""Generated from Smithy shape ``com.amazonaws.ram#ReplacePermissionAssociationsWorkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.replace_permission_associations_work

ReplacePermissionAssociationsWorkList: TypeAlias = list[
    "capo_ram.types.replace_permission_associations_work.ReplacePermissionAssociationsWork"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplacePermissionAssociationsWorkList) -> list:
    import capo_ram.types.replace_permission_associations_work

    out: list = []
    for item in value:
        out.append(
            capo_ram.types.replace_permission_associations_work.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReplacePermissionAssociationsWorkList:
    import capo_ram.types.replace_permission_associations_work

    out: ReplacePermissionAssociationsWorkList = []
    for item in data:
        out.append(
            capo_ram.types.replace_permission_associations_work.deserialize_json(item)
        )
    return out
