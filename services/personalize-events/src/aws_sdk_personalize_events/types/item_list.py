"""Generated from Smithy shape ``com.amazonaws.personalizeevents#ItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_events.types.item

ItemList: TypeAlias = list["aws_sdk_personalize_events.types.item.Item"]


# --- restJson1 ser/de ---
def serialize_json(value: ItemList) -> list:
    import aws_sdk_personalize_events.types.item

    out: list = []
    for item in value:
        out.append(aws_sdk_personalize_events.types.item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ItemList:
    import aws_sdk_personalize_events.types.item

    out: ItemList = []
    for item in data:
        out.append(aws_sdk_personalize_events.types.item.deserialize_json(item))
    return out
