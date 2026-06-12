"""Generated from Smithy shape ``com.amazonaws.devopsguru#TagHealths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.tag_health

TagHealths: TypeAlias = list["aws_sdk_devops_guru.types.tag_health.TagHealth"]


# --- restJson1 ser/de ---
def serialize_json(value: TagHealths) -> list:
    import aws_sdk_devops_guru.types.tag_health

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_guru.types.tag_health.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagHealths:
    import aws_sdk_devops_guru.types.tag_health

    out: TagHealths = []
    for item in data:
        out.append(aws_sdk_devops_guru.types.tag_health.deserialize_json(item))
    return out
