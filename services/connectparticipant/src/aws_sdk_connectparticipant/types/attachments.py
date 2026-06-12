"""Generated from Smithy shape ``com.amazonaws.connectparticipant#Attachments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.attachment_item

Attachments: TypeAlias = list[
    "aws_sdk_connectparticipant.types.attachment_item.AttachmentItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: Attachments) -> list:
    import aws_sdk_connectparticipant.types.attachment_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connectparticipant.types.attachment_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Attachments:
    import aws_sdk_connectparticipant.types.attachment_item

    out: Attachments = []
    for item in data:
        out.append(
            aws_sdk_connectparticipant.types.attachment_item.deserialize_json(item)
        )
    return out
