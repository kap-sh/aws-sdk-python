"""Generated from Smithy shape ``com.amazonaws.rbin#ResourceTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rbin.types.resource_tag

ResourceTags: TypeAlias = list["aws_sdk_rbin.types.resource_tag.ResourceTag"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTags) -> list:
    import aws_sdk_rbin.types.resource_tag

    out: list = []
    for item in value:
        out.append(aws_sdk_rbin.types.resource_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceTags:
    import aws_sdk_rbin.types.resource_tag

    out: ResourceTags = []
    for item in data:
        out.append(aws_sdk_rbin.types.resource_tag.deserialize_json(item))
    return out
