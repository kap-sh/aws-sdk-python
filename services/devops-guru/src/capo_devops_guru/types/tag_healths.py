"""Generated from Smithy shape ``com.amazonaws.devopsguru#TagHealths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.tag_health

TagHealths: TypeAlias = list["capo_devops_guru.types.tag_health.TagHealth"]


# --- restJson1 ser/de ---
def serialize_json(value: TagHealths) -> list:
    import capo_devops_guru.types.tag_health

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.tag_health.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagHealths:
    import capo_devops_guru.types.tag_health

    out: TagHealths = []
    for item in data:
        out.append(capo_devops_guru.types.tag_health.deserialize_json(item))
    return out
