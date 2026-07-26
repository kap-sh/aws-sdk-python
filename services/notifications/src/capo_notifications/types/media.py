"""Generated from Smithy shape ``com.amazonaws.notifications#Media``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.media_element

Media: TypeAlias = list["capo_notifications.types.media_element.MediaElement"]


# --- restJson1 ser/de ---
def serialize_json(value: Media) -> list:
    import capo_notifications.types.media_element

    out: list = []
    for item in value:
        out.append(capo_notifications.types.media_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> Media:
    import capo_notifications.types.media_element

    out: Media = []
    for item in data:
        out.append(capo_notifications.types.media_element.deserialize_json(item))
    return out
