"""Generated from Smithy shape ``com.amazonaws.notifications#Resources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.resource

Resources: TypeAlias = list["capo_notifications.types.resource.Resource"]


# --- restJson1 ser/de ---
def serialize_json(value: Resources) -> list:
    import capo_notifications.types.resource

    out: list = []
    for item in value:
        out.append(capo_notifications.types.resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> Resources:
    import capo_notifications.types.resource

    out: Resources = []
    for item in data:
        out.append(capo_notifications.types.resource.deserialize_json(item))
    return out
