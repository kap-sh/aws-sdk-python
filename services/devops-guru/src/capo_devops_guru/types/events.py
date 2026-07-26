"""Generated from Smithy shape ``com.amazonaws.devopsguru#Events``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.event

Events: TypeAlias = list["capo_devops_guru.types.event.Event"]


# --- restJson1 ser/de ---
def serialize_json(value: Events) -> list:
    import capo_devops_guru.types.event

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.event.serialize_json(item))
    return out


def deserialize_json(data: list) -> Events:
    import capo_devops_guru.types.event

    out: Events = []
    for item in data:
        out.append(capo_devops_guru.types.event.deserialize_json(item))
    return out
