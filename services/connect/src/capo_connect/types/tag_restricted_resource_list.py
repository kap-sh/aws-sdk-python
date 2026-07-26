"""Generated from Smithy shape ``com.amazonaws.connect#TagRestrictedResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.tag_restricted_resource_name

TagRestrictedResourceList: TypeAlias = list[
    "capo_connect.types.tag_restricted_resource_name.TagRestrictedResourceName"
]


# --- restJson1 ser/de ---
def serialize_json(value: TagRestrictedResourceList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagRestrictedResourceList:
    return list(data)
