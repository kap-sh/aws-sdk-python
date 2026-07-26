"""Generated from Smithy shape ``com.amazonaws.omics#TypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.share_resource_type

TypeList: TypeAlias = list["capo_omics.types.share_resource_type.ShareResourceType"]


# --- restJson1 ser/de ---
def serialize_json(value: TypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> TypeList:
    return list(data)
