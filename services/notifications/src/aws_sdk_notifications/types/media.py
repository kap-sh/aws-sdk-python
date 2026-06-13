"""Generated from Smithy shape ``com.amazonaws.notifications#Media``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_notifications.types.media_element

Media: TypeAlias = list["aws_sdk_notifications.types.media_element.MediaElement"]


# --- restJson1 ser/de ---
def serialize_json(value: Media) -> list:
    import aws_sdk_notifications.types.media_element

    out: list = []
    for item in value:
        out.append(aws_sdk_notifications.types.media_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> Media:
    import aws_sdk_notifications.types.media_element

    out: Media = []
    for item in data:
        out.append(aws_sdk_notifications.types.media_element.deserialize_json(item))
    return out
