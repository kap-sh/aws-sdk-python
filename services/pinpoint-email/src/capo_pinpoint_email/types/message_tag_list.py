"""Generated from Smithy shape ``com.amazonaws.pinpointemail#MessageTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_email.types.message_tag

MessageTagList: TypeAlias = list["capo_pinpoint_email.types.message_tag.MessageTag"]


# --- restJson1 ser/de ---
def serialize_json(value: MessageTagList) -> list:
    import capo_pinpoint_email.types.message_tag

    out: list = []
    for item in value:
        out.append(capo_pinpoint_email.types.message_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> MessageTagList:
    import capo_pinpoint_email.types.message_tag

    out: MessageTagList = []
    for item in data:
        out.append(capo_pinpoint_email.types.message_tag.deserialize_json(item))
    return out
