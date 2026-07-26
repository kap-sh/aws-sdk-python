"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfInAppMessageContent``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.in_app_message_content

ListOfInAppMessageContent: TypeAlias = list[
    "capo_pinpoint.types.in_app_message_content.InAppMessageContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfInAppMessageContent) -> list:
    import capo_pinpoint.types.in_app_message_content

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.in_app_message_content.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfInAppMessageContent:
    import capo_pinpoint.types.in_app_message_content

    out: ListOfInAppMessageContent = []
    for item in data:
        out.append(capo_pinpoint.types.in_app_message_content.deserialize_json(item))
    return out
