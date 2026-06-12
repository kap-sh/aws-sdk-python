"""Generated from Smithy shape ``com.amazonaws.connect#TagRestrictedResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.tag_restricted_resource_name

TagRestrictedResourceList: TypeAlias = list[
    "aws_sdk_connect.types.tag_restricted_resource_name.TagRestrictedResourceName"
]


# --- restJson1 ser/de ---
def serialize_json(value: TagRestrictedResourceList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagRestrictedResourceList:
    return list(data)
